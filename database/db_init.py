import os
import csv
import json
from models.schema import (
    db, Student, Branch, AcademicYear, Semester,
    Subject, Unit, Topic, Question, TestAttempt,
    TestResponse, TopicPerformance, Recommendation,
    LearningResource
)
from analysis.performance import analyze_attempt_responses
from ml.recommendation import generate_topic_recommendations

OFFICIAL_SUBJECT_CODES = {
    # Semester III
    "Engineering Mathematics-III": "25AF1000BS301",
    "Discrete Mathematics": "25AF1245PC303",
    "Data Structures": "25AF1245PC302",
    "Artificial Intelligence": "25AFAIPC304",
    "Prompt Engineering": "25AFAIPC307",
    # Semester IV
    "Introduction to Operating Systems": "25AFAIPC401",
    "Data Analytics": "25AFAIPC402",
    "Probability and Statistics": "25AF1245PC403",
    "Full Stack Development": "25AFAIPCL404",
    # Semester V
    "Machine Learning": "26AF1245PC501",
    "Object Oriented Programming in Java": "26AFAIPC502",
    "Cloud and Distributed AI Systems": "26AFAIPC503",
    "Data Engineering and Big Data Systems": "26AFAIPC504",
    "Vector Databases": "26AFAIPE507",
    # Semester VI
    "Deep Learning": "26AFAIPC601",
    "Natural Language Processing": "26AFAIPC602",
    "Fundamental Edge AI": "26AFAIPC603"
}

def init_database(app):
    """
    Initializes database tables and seeds academic structures,
    updated DBATU syllabus, and 60-question diagnostic pools per subject.
    """
    with app.app_context():
        db_path = app.config['DATABASE_PATH']
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        db.create_all()

        # 1. Seed Branches
        branches_data = [
            {"name": "Artificial Intelligence & Data Science", "code": "AI&DS"},
            {"name": "Computer Engineering", "code": "COMP"},
            {"name": "Information Technology", "code": "IT"},
            {"name": "Electronics & Telecommunication", "code": "EXTC"}
        ]
        branch_map = {}
        for b_data in branches_data:
            branch = Branch.query.filter_by(name=b_data['name']).first()
            if not branch:
                branch = Branch(name=b_data['name'], code=b_data['code'])
                db.session.add(branch)
                db.session.flush()
            branch_map[branch.name] = branch

        # 2. Seed Academic Years
        years_data = [
            {"name": "First Year", "year_number": 1},
            {"name": "Second Year", "year_number": 2},
            {"name": "Third Year", "year_number": 3},
            {"name": "Final Year", "year_number": 4}
        ]
        year_map = {}
        for y_data in years_data:
            year = AcademicYear.query.filter_by(name=y_data['name']).first()
            if not year:
                year = AcademicYear(name=y_data['name'], year_number=y_data['year_number'])
                db.session.add(year)
                db.session.flush()
            year_map[year.name] = year

        # 3. Seed All Semesters for AI&DS
        aids_branch = branch_map["Artificial Intelligence & Data Science"]
        sem_definitions = [
            ("Second Year", "Semester III", "SEM3"),
            ("Second Year", "Semester IV", "SEM4"),
            ("Third Year", "Semester V", "SEM5"),
            ("Third Year", "Semester VI", "SEM6"),
            ("Final Year", "Semester VII", "SEM7"),
            ("Final Year", "Semester VIII", "SEM8"),
        ]
        sem_map = {}
        for y_name, s_name, s_code in sem_definitions:
            y_obj = year_map[y_name]
            sem = Semester.query.filter_by(branch_id=aids_branch.id, year_id=y_obj.id, name=s_name).first()
            if not sem:
                sem = Semester(branch_id=aids_branch.id, year_id=y_obj.id, name=s_name, code=s_code)
                db.session.add(sem)
                db.session.flush()
            sem_map[s_name] = sem

        # 4. Seed Syllabus from CSV
        syllabus_csv = app.config['SYLLABUS_CSV']
        if os.path.exists(syllabus_csv):
            import_syllabus_from_csv(syllabus_csv, sem_map.get("Semester V").id if "Semester V" in sem_map else None)

        # 5. Seed Questions from CSV
        questions_csv = app.config['QUESTIONS_CSV']
        if os.path.exists(questions_csv):
            import_questions_from_csv(questions_csv)

        sem5 = sem_map.get("Semester V")
        third_year = year_map["Third Year"]

        # 6. Seed Admin Account
        admin = Student.query.filter_by(email="admin@college.edu").first()
        if not admin:
            admin = Student(
                student_id="ADMIN01",
                name="System Administrator",
                email="admin@college.edu",
                role="admin",
                branch_id=aids_branch.id,
                year_id=third_year.id,
                semester_id=sem5.id if sem5 else None
            )
            admin.set_password("admin123")
            db.session.add(admin)

        # 7. Seed Demo Student S001
        student_s001 = Student.query.filter_by(student_id="S001").first()
        if not student_s001:
            student_s001 = Student(
                student_id="S001",
                name="Aarav Sharma (S001)",
                email="s001@college.edu",
                role="student",
                branch_id=aids_branch.id,
                year_id=third_year.id,
                semester_id=sem5.id if sem5 else None
            )
            student_s001.set_password("password123")
            db.session.add(student_s001)
            db.session.flush()

            if sem5:
                seed_initial_attempt_for_s001(student_s001, sem5)

        db.session.commit()

        # Seed Verified Educational Resources
        try:
            from database.seed_educational_resources import seed_educational_resources
            seed_educational_resources()
        except Exception as e:
            print(f"[WARN] Resource seeding encountered: {e}")

        print("Database initialized successfully with updated DBATU syllabus.")


def import_syllabus_from_csv(csv_path, default_semester_id=None):
    """
    Imports DBATU syllabus records from CSV.
    Columns: branch,year,semester,subject,unit,topic,subtopic
    """
    if not os.path.exists(csv_path):
        return

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            branch_name = row.get('branch', 'Artificial Intelligence & Data Science').strip()
            year_name = row.get('year', 'Third Year').strip()
            semester_name = row.get('semester', 'Semester V').strip()
            subject_name = row.get('subject', '').strip()
            unit_title = row.get('unit', '').strip()
            topic_name = row.get('topic', '').strip()
            subtopics = row.get('subtopic', '').strip()

            if not subject_name or not topic_name:
                continue

            # Determine Target Semester
            target_sem = Semester.query.join(Branch).filter(
                Branch.name == branch_name,
                Semester.name == semester_name
            ).first()

            if not target_sem and default_semester_id:
                target_sem = Semester.query.get(default_semester_id)

            if not target_sem:
                target_sem = Semester.query.filter_by(name=semester_name).first()

            if not target_sem:
                continue

            # Find or create subject
            subject = Subject.query.filter_by(semester_id=target_sem.id, name=subject_name).first()
            if not subject:
                code = OFFICIAL_SUBJECT_CODES.get(
                    subject_name,
                    "".join([w[0] for w in subject_name.split() if w.isalnum()])[:4].upper() + "501"
                )
                subject = Subject(semester_id=target_sem.id, name=subject_name, code=code)
                db.session.add(subject)
                db.session.flush()
            elif not subject.code and subject_name in OFFICIAL_SUBJECT_CODES:
                subject.code = OFFICIAL_SUBJECT_CODES[subject_name]

            # Find or create unit
            unit = Unit.query.filter_by(subject_id=subject.id, unit_number=unit_title).first()
            if not unit:
                unit = Unit(subject_id=subject.id, unit_number=unit_title, title=unit_title)
                db.session.add(unit)
                db.session.flush()

            # Find or create topic
            topic = Topic.query.filter_by(unit_id=unit.id, name=topic_name).first()
            if not topic:
                topic = Topic(unit_id=unit.id, name=topic_name, subtopics=subtopics)
                db.session.add(topic)
                db.session.flush()
            elif subtopics and not topic.subtopics:
                topic.subtopics = subtopics


def import_questions_from_csv(csv_path):
    """
    Imports diagnostic questions from CSV.
    Columns: student_id,branch,year,semester,subject,unit,topic,question,option_a,option_b,option_c,option_d,correct_answer,difficulty
    """
    if not os.path.exists(csv_path):
        return

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            branch_name = row.get('branch', 'Artificial Intelligence & Data Science').strip()
            semester_name = row.get('semester', 'Semester V').strip()
            subject_name = row.get('subject', '').strip()
            unit_title = row.get('unit', '').strip()
            topic_name = row.get('topic', '').strip()
            question_text = row.get('question', '').strip()
            option_a = row.get('option_a', '').strip()
            option_b = row.get('option_b', '').strip()
            option_c = row.get('option_c', '').strip()
            option_d = row.get('option_d', '').strip()
            correct_answer = row.get('correct_answer', '').strip().upper()
            difficulty = row.get('difficulty', 'Medium').strip().capitalize()

            if not question_text or not topic_name:
                continue

            # Query the precise topic in this subject/semester
            topic = Topic.query.join(Unit).join(Subject).join(Semester).filter(
                Semester.name == semester_name,
                Subject.name == subject_name,
                Topic.name == topic_name
            ).first()

            if not topic:
                topic = Topic.query.filter_by(name=topic_name).first()

            if not topic:
                # Create subject/unit/topic if not yet loaded
                sem = Semester.query.filter_by(name=semester_name).first()
                if not sem:
                    sem = Semester.query.first()
                if sem:
                    subj = Subject.query.filter_by(semester_id=sem.id, name=subject_name).first()
                    if not subj:
                        code = OFFICIAL_SUBJECT_CODES.get(subject_name, "SUBJ501")
                        subj = Subject(semester_id=sem.id, name=subject_name, code=code)
                        db.session.add(subj)
                        db.session.flush()
                    unit = Unit.query.filter_by(subject_id=subj.id, unit_number=unit_title).first()
                    if not unit:
                        unit = Unit(subject_id=subj.id, unit_number=unit_title, title=unit_title)
                        db.session.add(unit)
                        db.session.flush()
                    topic = Topic(unit_id=unit.id, name=topic_name)
                    db.session.add(topic)
                    db.session.flush()

            if topic:
                existing_q = Question.query.filter_by(topic_id=topic.id, question_text=question_text).first()
                if not existing_q:
                    q = Question(
                        topic_id=topic.id,
                        question_text=question_text,
                        option_a=option_a,
                        option_b=option_b,
                        option_c=option_c,
                        option_d=option_d,
                        correct_answer=correct_answer,
                        difficulty=difficulty
                    )
                    db.session.add(q)


def seed_initial_attempt_for_s001(student, semester):
    """
    Creates a comprehensive initial attempt for S001 with realistic responses across Semester V subjects:
    Machine Learning, Object Oriented Programming in Java, Cloud and Distributed AI Systems,
    Data Engineering and Big Data Systems, and Vector Databases.
    Enables immediate demonstration of dashboard charts, topic performance, and AI recommendations.
    """
    # Sample a representative set of questions across all topics in Semester V
    topics = Topic.query.join(Unit).join(Subject).filter(
        Subject.semester_id == semester.id
    ).all()

    if not topics:
        return

    sample_questions = []
    # Pick 4 questions per topic across the 10 topics in Sem V = 40 questions total
    for top in topics:
        top_qs = Question.query.filter_by(topic_id=top.id).order_by(Question.id).limit(4).all()
        sample_questions.extend(top_qs)

    if not sample_questions:
        return

    attempt = TestAttempt(
        student_id=student.id,
        semester_id=semester.id,
        attempt_number=1,
        attempt_type='diagnostic',
        total_questions=len(sample_questions),
        correct_count=0,
        score_percentage=0.0
    )
    db.session.add(attempt)
    db.session.flush()

    # Define targets for realistic distribution:
    weak_target_topics = {
        "PAC Learning & VC Dimension",
        "PyTorch Distributed Data Parallel (DDP)",
        "ANN Indexing Algorithms (HNSW, IVF, PQ)"
    }
    strong_target_topics = {
        "Decision Trees & Instance-Based Learning",
        "Classes, Objects & OOP Principles",
        "Cloud Computing Fundamentals",
        "Vector Representations & Distance Metrics"
    }

    responses_data = []
    correct_total = 0

    for q in sample_questions:
        topic_name = q.topic_ref.name
        subject_name = q.topic_ref.unit_ref.subject_ref.name

        if topic_name in weak_target_topics:
            is_corr = (q.difficulty == 'Easy')
        elif topic_name in strong_target_topics:
            is_corr = True
        else:
            is_corr = (q.difficulty != 'Hard')

        selected_ans = q.correct_answer if is_corr else ('B' if q.correct_answer != 'B' else 'A')
        if is_corr:
            correct_total += 1

        resp = TestResponse(
            attempt_id=attempt.id,
            student_id=student.id,
            question_id=q.id,
            selected_answer=selected_ans,
            correct_answer=q.correct_answer,
            is_correct=is_corr
        )
        db.session.add(resp)

        responses_data.append({
            'question_id': q.id,
            'topic_id': q.topic_id,
            'topic_name': topic_name,
            'subject_id': q.topic_ref.unit_ref.subject_id,
            'subject_name': subject_name,
            'unit_number': q.topic_ref.unit_ref.unit_number,
            'difficulty': q.difficulty,
            'selected_answer': selected_ans,
            'correct_answer': q.correct_answer,
            'is_correct': is_corr
        })

    attempt.correct_count = correct_total
    attempt.score_percentage = round((correct_total / len(sample_questions)) * 100.0, 2)

    # Process with Pandas
    analysis_res = analyze_attempt_responses(responses_data)

    # Save topic performance & recommendations
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

        topic_obj = Topic.query.get(t['topic_id'])
        subtopics_str = topic_obj.subtopics if topic_obj else ""

        rec_data = generate_topic_recommendations(
            topic_name=t['topic_name'],
            subject_name=t['subject_name'],
            accuracy=t['accuracy'],
            classification=t['classification'],
            previous_score=attempt.score_percentage,
            attempt_number=attempt.attempt_number,
            correct=t['correct_answers'],
            total=t['total_questions'],
            subtopics=subtopics_str
        )

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
