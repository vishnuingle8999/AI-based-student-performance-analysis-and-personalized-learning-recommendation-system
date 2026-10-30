import os
import json
import functools
from flask import (
    Flask, render_template, request, redirect,
    url_for, flash, session, send_file, abort
)
from werkzeug.utils import secure_filename

from config import Config
from models.schema import (
    db, Student, Branch, AcademicYear, Semester,
    Subject, Unit, Topic, Question, TestAttempt,
    TestResponse, TopicPerformance, Recommendation,
    LearningResource
)
from database.db_init import (
    init_database, import_syllabus_from_csv, import_questions_from_csv
)
from analysis.performance import analyze_attempt_responses
from ml.recommendation import (
    generate_topic_recommendations, get_ml_classifier
)
from ml.nebius_tutor import generate_nebius_study_guidance
from ml.resource_ranking import (
    rank_resources_for_topic, generate_fallback_search_links
)

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database with tables & initial data
db.init_app(app)
with app.app_context():
    init_database(app)


# ----------------------------------------------------
# Authentication Decorators & Helpers
# ----------------------------------------------------
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view


def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' not in session or session.get('user_role') != 'admin':
            flash('Administrator privileges required.', 'danger')
            return redirect(url_for('index'))
        return view(**kwargs)
    return wrapped_view


def get_current_student():
    if 'user_id' in session:
        return db.session.get(Student, session['user_id'])
    return None


def get_current_semester(student):
    if not student:
        return None
    if student.semester_id:
        return db.session.get(Semester, student.semester_id)
    # Default fallback to first semester
    return Semester.query.first()


# ----------------------------------------------------
# Routes: Public & Authentication
# ----------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student_id = request.form.get('student_id', '').strip()
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        branch_id = request.form.get('branch_id', type=int)
        year_id = request.form.get('year_id', type=int)
        semester_id = request.form.get('semester_id', type=int)

        if not student_id or not name or not email or not password:
            flash('All required fields must be filled.', 'danger')
            return redirect(url_for('register'))

        if Student.query.filter_by(student_id=student_id).first():
            flash(f'Student ID "{student_id}" is already registered.', 'danger')
            return redirect(url_for('register'))

        if Student.query.filter_by(email=email).first():
            flash(f'Email "{email}" is already registered.', 'danger')
            return redirect(url_for('register'))

        learning_preference = request.form.get('learning_preference', 'both').strip().lower()
        if learning_preference not in ['notes', 'videos', 'both']:
            learning_preference = 'both'

        new_student = Student(
            student_id=student_id,
            name=name,
            email=email,
            branch_id=branch_id,
            year_id=year_id,
            semester_id=semester_id,
            role='student',
            learning_preference=learning_preference
        )
        new_student.set_password(password)
        db.session.add(new_student)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    branches = Branch.query.all()
    years = AcademicYear.query.order_by(AcademicYear.year_number).all()
    semesters = Semester.query.all()
    return render_template('register.html', branches=branches, years=years, semesters=semesters)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_identifier = request.form.get('login_identifier', '').strip()
        password = request.form.get('password', '')

        # Search by student_id or email
        user = Student.query.filter(
            (Student.student_id == login_identifier) | (Student.email == login_identifier.lower())
        ).first()

        if user and user.check_password(password):
            session.clear()
            session['user_id'] = user.id
            session['student_id'] = user.student_id
            session['user_name'] = user.name
            session['user_role'] = user.role
            if user.semester_ref:
                session['semester_id'] = user.semester_ref.id
                session['semester_name'] = user.semester_ref.name
                session['branch_code'] = user.branch_ref.code if user.branch_ref else 'AI&DS'

            flash(f'Welcome back, {user.name}!', 'success')
            if user.role == 'admin':
                return redirect(url_for('admin_view'))
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid login identifier or password. Try demo credentials: S001 / password123', 'danger')

    return render_template('login.html')


@app.route('/demo-login')
def quick_demo_login():
    """Quick one-click login as demo student S001 for viva presentation."""
    user = Student.query.filter_by(student_id="S001").first()
    if user:
        session.clear()
        session['user_id'] = user.id
        session['student_id'] = user.student_id
        session['user_name'] = user.name
        session['user_role'] = user.role
        if user.semester_ref:
            session['semester_id'] = user.semester_ref.id
            session['semester_name'] = user.semester_ref.name
            session['branch_code'] = user.branch_ref.code if user.branch_ref else 'AI&DS'
        flash('Logged in as demo student S001.', 'success')
        return redirect(url_for('dashboard'))
    flash('Demo user not found.', 'danger')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('index'))


# ----------------------------------------------------
# Routes: Academic Profile & Scope Switcher
# ----------------------------------------------------
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_view():
    student = get_current_student()
    if request.method == 'POST':
        branch_id = request.form.get('branch_id', type=int)
        year_id = request.form.get('year_id', type=int)
        semester_id = request.form.get('semester_id', type=int)
        learning_preference = request.form.get('learning_preference', '').strip().lower()

        student.branch_id = branch_id
        student.year_id = year_id
        student.semester_id = semester_id
        if learning_preference in ['notes', 'videos', 'both']:
            student.learning_preference = learning_preference
        db.session.commit()

        # Update session
        sem = db.session.get(Semester, semester_id)
        if sem:
            session['semester_id'] = sem.id
            session['semester_name'] = sem.name
            session['branch_code'] = sem.branch.code

        flash('Academic profile and learning preferences updated successfully.', 'success')
        return redirect(url_for('profile_view'))

    branches = Branch.query.all()
    years = AcademicYear.query.order_by(AcademicYear.year_number).all()
    semesters = Semester.query.all()
    return render_template('profile.html', student=student, branches=branches, years=years, semesters=semesters)


@app.route('/preferences/update', methods=['POST'])
@login_required
def update_learning_preference():
    student = get_current_student()
    if not student:
        flash('Student record not found.', 'danger')
        return redirect(url_for('login'))

    preference = request.form.get('learning_preference', '').strip().lower()
    if preference not in ['notes', 'videos', 'both']:
        flash('Invalid learning preference option selected.', 'danger')
        return redirect(request.referrer or url_for('recommendations_view'))

    student.learning_preference = preference
    db.session.commit()

    pref_labels = {
        'notes': 'Theory Notes & Code Walkthroughs',
        'videos': 'Video Lectures & Visual Demonstrations',
        'both': 'Both Notes and Video Lectures'
    }
    flash(f'Learning preference updated to "{pref_labels.get(preference)}" successfully!', 'success')
    return redirect(request.referrer or url_for('recommendations_view'))


# ----------------------------------------------------
# Routes: Syllabus
# ----------------------------------------------------
@app.route('/syllabus')
@login_required
def syllabus_view():
    student = get_current_student()
    req_sem_id = request.args.get('semester_id', type=int)
    if req_sem_id:
        semester = db.session.get(Semester, req_sem_id)
    else:
        semester = get_current_semester(student)

    if not semester:
        flash('Please select an academic semester in your profile.', 'warning')
        return redirect(url_for('profile_view'))

    all_semesters = Semester.query.order_by(Semester.id).all()
    # Crucial requirement: Load ONLY subjects belonging to the selected semester!
    subjects = Subject.query.filter_by(semester_id=semester.id).all()
    return render_template(
        'syllabus.html',
        student=student,
        semester=semester,
        subjects=subjects,
        all_semesters=all_semesters
    )


# ----------------------------------------------------
# Routes: Diagnostic Test & Assessment
# ----------------------------------------------------
@app.route('/test')
@login_required
def take_test():
    student = get_current_student()
    semester = get_current_semester(student)

    if not semester:
        flash('Please select your semester before attempting the test.', 'warning')
        return redirect(url_for('profile_view'))

    is_retest = request.args.get('retest') == '1'
    subject_id = request.args.get('subject_id', type=int)

    # All subjects for this semester (to allow subject-specific testing)
    semester_subjects = Subject.query.filter_by(semester_id=semester.id).all()

    query = Question.query.join(Topic).join(Unit).join(Subject).filter(
        Subject.semester_id == semester.id
    )

    selected_subject = None
    if subject_id:
        selected_subject = db.session.get(Subject, subject_id)
        if selected_subject and selected_subject.semester_id == semester.id:
            query = query.filter(Subject.id == subject_id)
        else:
            selected_subject = None
            subject_id = None

    questions = query.order_by(Subject.id, Topic.id, Question.id).all()

    return render_template(
        'test.html',
        student=student,
        semester=semester,
        questions=questions,
        semester_subjects=semester_subjects,
        selected_subject=selected_subject,
        subject_id=subject_id,
        is_retest=is_retest
    )


@app.route('/test/submit', methods=['POST'])
@login_required
def submit_test():
    student = get_current_student()
    semester_id = request.form.get('semester_id', type=int)
    subject_id = request.form.get('subject_id', type=int)
    is_retest_flag = request.form.get('is_retest') == '1'

    # Determine attempt number
    previous_attempts_count = TestAttempt.query.filter_by(
        student_id=student.id, semester_id=semester_id
    ).count()

    attempt_number = previous_attempts_count + 1
    attempt_type = 'retest' if is_retest_flag or previous_attempts_count > 0 else 'diagnostic'

    # Fetch questions for this test scope
    query = Question.query.join(Topic).join(Unit).join(Subject).filter(
        Subject.semester_id == semester_id
    )
    if subject_id:
        query = query.filter(Subject.id == subject_id)

    questions = query.all()

    if not questions:
        flash('No questions found for submission.', 'danger')
        return redirect(url_for('dashboard'))

    # Create new TestAttempt
    attempt = TestAttempt(
        student_id=student.id,
        semester_id=semester_id,
        attempt_number=attempt_number,
        attempt_type=attempt_type,
        total_questions=len(questions),
        correct_count=0,
        score_percentage=0.0
    )
    db.session.add(attempt)
    db.session.flush()

    responses_data = []
    correct_count = 0

    for q in questions:
        selected_answer = request.form.get(f'question_{q.id}')
        is_correct = (selected_answer == q.correct_answer) if selected_answer else False
        if is_correct:
            correct_count += 1

        resp = TestResponse(
            attempt_id=attempt.id,
            student_id=student.id,
            question_id=q.id,
            selected_answer=selected_answer,
            correct_answer=q.correct_answer,
            is_correct=is_correct
        )
        db.session.add(resp)

        responses_data.append({
            'question_id': q.id,
            'topic_id': q.topic_id,
            'topic_name': q.topic_ref.name,
            'subject_id': q.topic_ref.unit_ref.subject_id,
            'subject_name': q.topic_ref.unit_ref.subject_ref.name,
            'unit_number': q.topic_ref.unit_ref.unit_number,
            'difficulty': q.difficulty,
            'selected_answer': selected_answer,
            'correct_answer': q.correct_answer,
            'is_correct': is_correct
        })

    # Update attempt summary
    attempt.correct_count = correct_count
    attempt.score_percentage = round((correct_count / len(questions)) * 100.0, 2)

    # Performance analysis via Pandas
    analysis_res = analyze_attempt_responses(responses_data)

    # Fetch previous attempt score for ML feature context
    prev_attempt = TestAttempt.query.filter(
        TestAttempt.student_id == student.id,
        TestAttempt.semester_id == semester_id,
        TestAttempt.id != attempt.id
    ).order_by(TestAttempt.created_at.desc()).first()
    prev_score = prev_attempt.score_percentage if prev_attempt else attempt.score_percentage

    # Save topic performance and generate personalized recommendations
    for t in analysis_res['topics']:
        tp = TopicPerformance(
            attempt_id=attempt.id,
            student_id=student.id,
            topic_id=t['topic_id'],
            total_questions=t['total_questions'],
            correct_count=t['correct_answers'],
            accuracy_percentage=t['accuracy'],
            classification=t['classification']
        )
        db.session.add(tp)

        # Lookup subtopics from Topic model
        topic_obj = db.session.get(Topic, t['topic_id'])
        subtopics_str = topic_obj.subtopics if topic_obj else ""

        # AI Recommendation generation (Decision Tree + Rules)
        rec_data = generate_topic_recommendations(
            topic_name=t['topic_name'],
            subject_name=t['subject_name'],
            accuracy=t['accuracy'],
            classification=t['classification'],
            previous_score=prev_score,
            attempt_number=attempt.attempt_number,
            correct=t['correct_answers'],
            total=t['total_questions'],
            subtopics=subtopics_str
        )

        # Generate additional personalised guidance using Nebius AI.
        # If Nebius is unavailable, the existing recommendations still work.
        nebius_result = generate_nebius_study_guidance(
            topic_name=t['topic_name'],
            subject_name=t['subject_name'],
            accuracy=t['accuracy'],
            classification=t['classification'],
            existing_plan=rec_data.get('steps', [])
        )
        rec_data['ai_guidance'] = nebius_result

        rec = Recommendation(
            attempt_id=attempt.id,
            student_id=student.id,
            topic_id=t['topic_id'],
            classification=t['classification'],
            predicted_requirement=rec_data['predicted_requirement'],
            recommendation_title=rec_data['title'],
            recommendation_text=rec_data['ml_explanation'],
            study_resources_json=json.dumps(rec_data)
        )
        db.session.add(rec)

    db.session.commit()
    flash('Assessment submitted and analyzed successfully by AI!', 'success')
    return redirect(url_for('test_result', attempt_id=attempt.id))


@app.route('/test/result/<int:attempt_id>')
@login_required
def test_result(attempt_id):
    attempt = db.get_or_404(TestAttempt, attempt_id)
    if attempt.student_id != session['user_id'] and session.get('user_role') != 'admin':
        abort(403)

    # Reconstruct summaries from responses and topic_performances
    topic_perfs = TopicPerformance.query.filter_by(attempt_id=attempt.id).all()
    topics_summary = []
    weak_count = 0
    strong_count = 0

    for tp in topic_perfs:
        if tp.classification == 'WEAK':
            weak_count += 1
        elif tp.classification == 'STRONG':
            strong_count += 1

        topics_summary.append({
            'topic_id': tp.topic_id,
            'topic_name': tp.topic_ref.name,
            'subject_name': tp.topic_ref.unit_ref.subject_ref.name,
            'total_questions': tp.total_questions,
            'correct_answers': tp.correct_count,
            'accuracy': tp.accuracy_percentage,
            'classification': tp.classification
        })

    # Sort weakest first
    topics_summary.sort(key=lambda x: x['accuracy'])

    # Subject-wise summary
    subject_map = {}
    for resp in attempt.responses:
        s_name = resp.question_ref.topic_ref.unit_ref.subject_ref.name
        if s_name not in subject_map:
            subject_map[s_name] = {'total_questions': 0, 'correct_answers': 0}
        subject_map[s_name]['total_questions'] += 1
        if resp.is_correct:
            subject_map[s_name]['correct_answers'] += 1

    subjects_summary = []
    for s_name, data in subject_map.items():
        acc = round((data['correct_answers'] / data['total_questions']) * 100.0, 2) if data['total_questions'] > 0 else 0.0
        subjects_summary.append({
            'subject_name': s_name,
            'total_questions': data['total_questions'],
            'correct_answers': data['correct_answers'],
            'accuracy': acc
        })

    return render_template(
        'result.html',
        attempt=attempt,
        subjects_summary=subjects_summary,
        topics_summary=topics_summary,
        weak_count=weak_count,
        strong_count=strong_count
    )


# ----------------------------------------------------
# Routes: Personalized Dashboard & Visualizations
# ----------------------------------------------------
@app.route('/dashboard')
@login_required
def dashboard():
    student = get_current_student()
    semester = get_current_semester(student)

    # Get latest attempt
    latest_attempt = TestAttempt.query.filter_by(
        student_id=student.id, semester_id=semester.id if semester else None
    ).order_by(TestAttempt.created_at.desc()).first()

    # Get all attempts for progression tracking
    attempts = TestAttempt.query.filter_by(
        student_id=student.id, semester_id=semester.id if semester else None
    ).order_by(TestAttempt.created_at.asc()).all()

    subjects_summary = []
    topics_summary = []
    weak_topics = []
    counts = {'weak': 0, 'average': 0, 'strong': 0}
    improvement = 0.0

    if latest_attempt:
        topic_perfs = TopicPerformance.query.filter_by(attempt_id=latest_attempt.id).all()
        for tp in topic_perfs:
            entry = {
                'topic_id': tp.topic_id,
                'topic_name': tp.topic_ref.name,
                'subject_name': tp.topic_ref.unit_ref.subject_ref.name,
                'total_questions': tp.total_questions,
                'correct_answers': tp.correct_count,
                'accuracy': tp.accuracy_percentage,
                'classification': tp.classification
            }
            topics_summary.append(entry)
            if tp.classification == 'WEAK':
                counts['weak'] += 1
                weak_topics.append(entry)
            elif tp.classification == 'AVERAGE':
                counts['average'] += 1
            else:
                counts['strong'] += 1

        # Sort weakest first
        topics_summary.sort(key=lambda x: x['accuracy'])
        weak_topics.sort(key=lambda x: x['accuracy'])

        # Aggregate subject performance for chart
        subject_map = {}
        for tp in topic_perfs:
            s_name = tp.topic_ref.unit_ref.subject_ref.name
            if s_name not in subject_map:
                subject_map[s_name] = {'correct': 0, 'total': 0}
            subject_map[s_name]['correct'] += tp.correct_count
            subject_map[s_name]['total'] += tp.total_questions

        for s_name, data in subject_map.items():
            acc = round((data['correct'] / data['total']) * 100.0, 2) if data['total'] > 0 else 0.0
            subjects_summary.append({
                'subject_name': s_name,
                'accuracy': acc
            })

        # Calculate improvement percentage points between first and latest attempt
        if len(attempts) > 1:
            baseline = attempts[0].score_percentage
            current = latest_attempt.score_percentage
            improvement = round(current - baseline, 2)

    attempts_summary = [
        {
            'attempt_number': a.attempt_number,
            'attempt_type': a.attempt_type,
            'score_percentage': a.score_percentage,
            'date': a.created_at.strftime('%b %d')
        }
        for a in attempts
    ]

    return render_template(
        'dashboard.html',
        student=student,
        semester=semester,
        latest_attempt=latest_attempt,
        attempts=attempts,
        subjects_summary=subjects_summary,
        topics_summary=topics_summary,
        weak_topics=weak_topics,
        counts=counts,
        improvement=improvement,
        attempts_summary=attempts_summary
    )


# ----------------------------------------------------
# Routes: Personalized Recommendations
# ----------------------------------------------------
@app.route('/recommendations')
@login_required
def recommendations_view():
    student = get_current_student()
    semester = get_current_semester(student)

    latest_attempt = TestAttempt.query.filter_by(
        student_id=student.id, semester_id=semester.id if semester else None
    ).order_by(TestAttempt.created_at.desc()).first()

    recommendations_list = []
    weak_count = 0
    avg_count = 0
    strong_count = 0
    pref = student.learning_preference if student and student.learning_preference else 'both'

    if latest_attempt:
        recs = Recommendation.query.filter_by(attempt_id=latest_attempt.id).all()
        for r in recs:
            parsed_data = json.loads(r.study_resources_json) if r.study_resources_json else {}
            parsed_data['topic_id'] = r.topic_id
            if r.topic_ref and r.topic_ref.unit_ref:
                parsed_data['subject_id'] = r.topic_ref.unit_ref.subject_id

            # Query database for verified educational resources linked to this topic
            db_resources = LearningResource.query.filter_by(topic_id=r.topic_id).all()

            # Rank resources with intelligent preference & difficulty engine
            ranked_res = rank_resources_for_topic(
                resources=db_resources,
                student_preference=pref,
                topic_accuracy=parsed_data.get('accuracy', 50.0),
                topic_name=parsed_data.get('topic_name', ''),
                subject_name=parsed_data.get('subject_name', '')
            )

            # Generate fallback search options
            fallbacks = generate_fallback_search_links(
                topic_name=parsed_data.get('topic_name', ''),
                subject_name=parsed_data.get('subject_name', ''),
                student_preference=pref
            )

            parsed_data['educational_resources'] = ranked_res
            parsed_data['fallback_search_links'] = fallbacks
            parsed_data['has_verified_resources'] = (len(ranked_res) > 0)

            recommendations_list.append(parsed_data)
            if r.classification == 'WEAK':
                weak_count += 1
            elif r.classification == 'AVERAGE':
                avg_count += 1
            else:
                strong_count += 1

        # Sort: WEAKEST topics first!
        recommendations_list.sort(key=lambda x: x.get('accuracy', 0))

    # Get ML feature importances for viva defense
    ml_classifier = get_ml_classifier()
    feature_importances = ml_classifier.get_feature_importances()

    return render_template(
        'recommendations.html',
        student=student,
        semester=semester,
        recommendations=recommendations_list,
        weak_count=weak_count,
        avg_count=avg_count,
        strong_count=strong_count,
        feature_importances=feature_importances,
        active_preference=pref
    )


# ----------------------------------------------------
# Routes: Progress Tracking & Re-test Comparison
# ----------------------------------------------------
@app.route('/progress')
@login_required
def progress_view():
    student = get_current_student()
    semester = get_current_semester(student)

    attempts = TestAttempt.query.filter_by(
        student_id=student.id, semester_id=semester.id if semester else None
    ).order_by(TestAttempt.created_at.desc()).all()

    previous_score = 0.0
    current_score = 0.0
    improvement = 0.0

    if attempts:
        current_score = attempts[0].score_percentage
        # Earliest or previous attempt
        previous_score = attempts[-1].score_percentage if len(attempts) > 1 else current_score
        improvement = round(current_score - previous_score, 2)

    # Chronological order for Chart.js
    attempts_chronological = sorted(attempts, key=lambda a: a.created_at)
    attempts_summary = [
        {
            'attempt_number': a.attempt_number,
            'attempt_type': a.attempt_type,
            'score_percentage': a.score_percentage,
            'date': a.created_at.strftime('%b %d')
        }
        for a in attempts_chronological
    ]

    return render_template(
        'progress.html',
        student=student,
        semester=semester,
        attempts=attempts,
        previous_score=previous_score,
        current_score=current_score,
        improvement=improvement,
        attempts_summary=attempts_summary
    )


# ----------------------------------------------------
# Routes: Administrator Portal & CSV Management
# ----------------------------------------------------
@app.route('/admin')
@admin_required
def admin_view():
    stats = {
        'total_students': Student.query.filter_by(role='student').count(),
        'total_subjects': Subject.query.count(),
        'total_topics': Topic.query.count(),
        'total_questions': Question.query.count(),
        'total_resources': LearningResource.query.count()
    }
    students = Student.query.all()
    semesters = Semester.query.all()
    topics = Topic.query.all()
    # List all subjects ordered by semester and name
    subjects = Subject.query.join(Semester).order_by(Semester.id, Subject.name).all()
    resources = LearningResource.query.join(Topic).join(Unit).join(Subject).order_by(Subject.name, Topic.name, LearningResource.id).all()
    return render_template(
        'admin.html',
        stats=stats,
        students=students,
        semesters=semesters,
        topics=topics,
        subjects=subjects,
        resources=resources
    )


@app.route('/admin/upload-questions', methods=['POST'])
@admin_required
def admin_upload_questions():
    file = request.files.get('csv_file')
    if not file or not file.filename.endswith('.csv'):
        flash('Please select a valid CSV file.', 'danger')
        return redirect(url_for('admin_view'))

    filename = secure_filename(file.filename)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'], f'questions_upload_{filename}')
    file.save(temp_path)

    try:
        import_questions_from_csv(temp_path)
        db.session.commit()
        flash('Question bank successfully imported from CSV!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error importing questions: {str(e)}', 'danger')

    return redirect(url_for('admin_view'))


@app.route('/admin/upload-syllabus', methods=['POST'])
@admin_required
def admin_upload_syllabus():
    semester_id = request.form.get('semester_id', type=int)
    file = request.files.get('csv_file')
    if not file or not file.filename.endswith('.csv'):
        flash('Please select a valid CSV file.', 'danger')
        return redirect(url_for('admin_view'))

    filename = secure_filename(file.filename)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'], f'syllabus_upload_{filename}')
    file.save(temp_path)

    try:
        import_syllabus_from_csv(temp_path, semester_id)
        db.session.commit()
        flash('Syllabus data successfully imported from CSV!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error importing syllabus: {str(e)}', 'danger')

    return redirect(url_for('admin_view'))


@app.route('/admin/add-subject', methods=['POST'])
@admin_required
def admin_add_subject():
    semester_id = request.form.get('semester_id', type=int)
    subject_name = request.form.get('subject_name', '').strip()
    subject_code = request.form.get('subject_code', '').strip()
    redirect_target = request.form.get('next') or request.referrer or url_for('admin_view')

    if not semester_id or not subject_name:
        flash('Semester and Subject Name are required.', 'danger')
        return redirect(redirect_target)

    # Check for duplicate in this semester
    existing = Subject.query.filter_by(semester_id=semester_id, name=subject_name).first()
    if existing:
        flash(f'Subject "{subject_name}" already exists in this semester.', 'warning')
        return redirect(redirect_target)

    if not subject_code:
        from database.db_init import OFFICIAL_SUBJECT_CODES
        subject_code = OFFICIAL_SUBJECT_CODES.get(
            subject_name,
            "".join([w[0] for w in subject_name.split() if w.isalnum()])[:4].upper() + "501"
        )
    else:
        subject_code = subject_code.upper()

    new_subj = Subject(semester_id=semester_id, name=subject_name, code=subject_code)
    db.session.add(new_subj)
    db.session.commit()
    flash(f'Subject "{subject_name}" ({subject_code}) added successfully.', 'success')
    return redirect(redirect_target)


@app.route('/admin/delete-subject/<int:subject_id>', methods=['POST'])
@admin_required
def admin_delete_subject(subject_id):
    subject = db.get_or_404(Subject, subject_id)
    subject_name = subject.name
    redirect_target = request.form.get('next') or request.referrer or url_for('admin_view')

    try:
        # Cascade cleanups for related records
        for unit in subject.units:
            for topic in unit.topics:
                for q in topic.questions:
                    TestResponse.query.filter_by(question_id=q.id).delete()
                TopicPerformance.query.filter_by(topic_id=topic.id).delete()
                Recommendation.query.filter_by(topic_id=topic.id).delete()
        db.session.delete(subject)
        db.session.commit()
        flash(f'Subject "{subject_name}" and its associated units/questions were deleted successfully.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting subject "{subject_name}": {str(e)}', 'danger')

    return redirect(redirect_target)


@app.route('/admin/add-question', methods=['POST'])
@admin_required
def admin_add_question():
    topic_id = request.form.get('topic_id', type=int)
    difficulty = request.form.get('difficulty', 'Medium')
    question_text = request.form.get('question_text', '').strip()
    option_a = request.form.get('option_a', '').strip()
    option_b = request.form.get('option_b', '').strip()
    option_c = request.form.get('option_c', '').strip()
    option_d = request.form.get('option_d', '').strip()
    correct_answer = request.form.get('correct_answer', 'A')

    if topic_id and question_text and option_a and option_b and option_c and option_d:
        q = Question(
            topic_id=topic_id,
            difficulty=difficulty,
            question_text=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_answer=correct_answer
        )
        db.session.add(q)
        db.session.commit()
        flash('Question added to database successfully.', 'success')
    return redirect(url_for('admin_view'))


@app.route('/admin/sample-questions.csv')
@admin_required
def download_sample_questions():
    csv_path = app.config['QUESTIONS_CSV']
    if os.path.exists(csv_path):
        return send_file(csv_path, as_attachment=True, download_name='sample_questions.csv')
    abort(404)


@app.route('/admin/sample-syllabus.csv')
@admin_required
def download_sample_syllabus():
    csv_path = app.config['SYLLABUS_CSV']
    if os.path.exists(csv_path):
        return send_file(csv_path, as_attachment=True, download_name='sample_syllabus.csv')
    abort(404)


@app.route('/admin/add-resource', methods=['POST'])
@admin_required
def admin_add_resource():
    topic_id = request.form.get('topic_id', type=int)
    title = request.form.get('title', '').strip()
    provider = request.form.get('provider', '').strip()
    resource_type = request.form.get('resource_type', 'notes').strip().lower()
    resource_url = request.form.get('resource_url', '').strip()
    description = request.form.get('description', '').strip()
    language = request.form.get('language', 'English').strip()
    difficulty = request.form.get('difficulty', 'Beginner').strip()
    verification_status = request.form.get('verification_status', 'verified').strip()

    if not topic_id or not title or not provider or not resource_url:
        flash('Topic, Title, Provider, and URL are required fields.', 'danger')
        return redirect(url_for('admin_view'))

    if resource_type not in ['notes', 'video', 'documentation', 'practice']:
        resource_type = 'notes'

    new_res = LearningResource(
        topic_id=topic_id,
        title=title,
        provider=provider,
        resource_type=resource_type,
        resource_url=resource_url,
        description=description,
        language=language,
        difficulty=difficulty,
        verification_status=verification_status
    )
    db.session.add(new_res)
    db.session.commit()
    flash(f'Educational resource "{title}" added successfully.', 'success')
    return redirect(url_for('admin_view'))


@app.route('/admin/delete-resource/<int:resource_id>', methods=['POST'])
@admin_required
def admin_delete_resource(resource_id):
    res = db.get_or_404(LearningResource, resource_id)
    res_title = res.title
    db.session.delete(res)
    db.session.commit()
    flash(f'Learning resource "{res_title}" removed.', 'success')
    return redirect(url_for('admin_view'))


@app.route('/admin/toggle-verify-resource/<int:resource_id>', methods=['POST'])
@admin_required
def admin_toggle_verify_resource(resource_id):
    res = db.get_or_404(LearningResource, resource_id)
    res.verification_status = 'unverified' if res.verification_status == 'verified' else 'verified'
    db.session.commit()
    flash(f'Resource "{res.title}" verification status set to "{res.verification_status}".', 'info')
    return redirect(url_for('admin_view'))


@app.route('/admin/reset-seed')
@admin_required
def admin_reset_seed():
    db.drop_all()
    init_database(app)
    flash('Database reset and re-seeded with demo data successfully!', 'success')
    return redirect(url_for('admin_view'))


# ----------------------------------------------------
# Error Handlers
# ----------------------------------------------------
@app.errorhandler(404)
def not_found(e):
    return render_template('base.html', error_code=404, error_msg="Page Not Found"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('base.html', error_code=500, error_msg="Internal Server Error"), 500


if __name__ == '__main__':
    print("Starting AI-Based Personalized Student Learning Recommendation System...")
    app.run(debug=True, host='127.0.0.1', port=5000)
