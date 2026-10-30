from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Branch(db.Model):
    __tablename__ = 'branches'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)

    semesters = db.relationship('Semester', backref='branch', lazy=True, cascade='all, delete-orphan')
    students = db.relationship('Student', backref='branch_ref', lazy=True)

    def __repr__(self):
        return f'<Branch {self.name}>'


class AcademicYear(db.Model):
    __tablename__ = 'years'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)  # e.g., 'Third Year'
    year_number = db.Column(db.Integer, nullable=False)           # e.g., 3

    semesters = db.relationship('Semester', backref='year_ref', lazy=True, cascade='all, delete-orphan')
    students = db.relationship('Student', backref='year_ref', lazy=True)

    def __repr__(self):
        return f'<AcademicYear {self.name}>'


class Semester(db.Model):
    __tablename__ = 'semesters'
    id = db.Column(db.Integer, primary_key=True)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'), nullable=False)
    year_id = db.Column(db.Integer, db.ForeignKey('years.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)  # e.g., 'Semester V'
    code = db.Column(db.String(20), nullable=False)  # e.g., 'SEM5'

    subjects = db.relationship('Subject', backref='semester_ref', lazy=True, cascade='all, delete-orphan')
    students = db.relationship('Student', backref='semester_ref', lazy=True)
    test_attempts = db.relationship('TestAttempt', backref='semester_ref', lazy=True)

    def __repr__(self):
        return f'<Semester {self.name} ({self.branch.code})>'


class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    semester_id = db.Column(db.Integer, db.ForeignKey('semesters.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(30), nullable=True)

    units = db.relationship('Unit', backref='subject_ref', lazy=True, cascade='all, delete-orphan')

    @property
    def question_count(self):
        return sum(len(topic.questions) for unit in self.units for topic in unit.topics)

    @property
    def topic_count(self):
        return sum(len(unit.topics) for unit in self.units)

    def __repr__(self):
        return f'<Subject {self.name}>'


class Unit(db.Model):
    __tablename__ = 'units'
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    unit_number = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(200), nullable=True)

    topics = db.relationship('Topic', backref='unit_ref', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Unit {self.unit_number}: {self.title}>'


class Topic(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    subtopics = db.Column(db.Text, nullable=True)

    questions = db.relationship('Question', backref='topic_ref', lazy=True, cascade='all, delete-orphan')
    topic_performances = db.relationship('TopicPerformance', backref='topic_ref', lazy=True, cascade='all, delete-orphan')
    recommendations = db.relationship('Recommendation', backref='topic_ref', lazy=True, cascade='all, delete-orphan')
    resources = db.relationship('LearningResource', backref='topic_ref', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Topic {self.name}>'


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    correct_answer = db.Column(db.String(5), nullable=False)  # 'A', 'B', 'C', 'D'
    difficulty = db.Column(db.String(20), nullable=False, default='Medium')  # 'Easy', 'Medium', 'Hard'

    responses = db.relationship('TestResponse', backref='question_ref', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Question {self.id}: {self.question_text[:30]}...>'


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(50), unique=True, nullable=False)  # e.g., 'S001'
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student')  # 'student' or 'admin'
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'), nullable=True)
    year_id = db.Column(db.Integer, db.ForeignKey('years.id'), nullable=True)
    semester_id = db.Column(db.Integer, db.ForeignKey('semesters.id'), nullable=True)
    learning_preference = db.Column(db.String(20), nullable=False, default='both')  # 'notes', 'videos', 'both'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    test_attempts = db.relationship('TestAttempt', backref='student_ref', lazy=True, cascade='all, delete-orphan')
    responses = db.relationship('TestResponse', backref='student_ref', lazy=True, cascade='all, delete-orphan')
    topic_performances = db.relationship('TopicPerformance', backref='student_ref', lazy=True, cascade='all, delete-orphan')
    recommendations = db.relationship('Recommendation', backref='student_ref', lazy=True, cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Student {self.student_id} - {self.name}>'


class TestAttempt(db.Model):
    __tablename__ = 'test_attempts'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    semester_id = db.Column(db.Integer, db.ForeignKey('semesters.id'), nullable=False)
    attempt_number = db.Column(db.Integer, nullable=False, default=1)
    attempt_type = db.Column(db.String(30), nullable=False, default='diagnostic')  # 'diagnostic' or 'retest'
    total_questions = db.Column(db.Integer, nullable=False, default=0)
    correct_count = db.Column(db.Integer, nullable=False, default=0)
    score_percentage = db.Column(db.Float, nullable=False, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    responses = db.relationship('TestResponse', backref='attempt_ref', lazy=True, cascade='all, delete-orphan')
    topic_performances = db.relationship('TopicPerformance', backref='attempt_ref', lazy=True, cascade='all, delete-orphan')
    recommendations = db.relationship('Recommendation', backref='attempt_ref', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<TestAttempt {self.id} Student {self.student_id} Score {self.score_percentage}%>'


class TestResponse(db.Model):
    __tablename__ = 'responses'
    id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey('test_attempts.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    selected_answer = db.Column(db.String(5), nullable=True)  # 'A', 'B', 'C', 'D' or None
    correct_answer = db.Column(db.String(5), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False, default=False)
    answered_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Response {self.id}: Q{self.question_id} ({self.selected_answer}) - Correct: {self.is_correct}>'


class TopicPerformance(db.Model):
    __tablename__ = 'topic_performances'
    id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey('test_attempts.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    total_questions = db.Column(db.Integer, nullable=False, default=0)
    correct_count = db.Column(db.Integer, nullable=False, default=0)
    accuracy_percentage = db.Column(db.Float, nullable=False, default=0.0)
    classification = db.Column(db.String(20), nullable=False)  # 'WEAK', 'AVERAGE', 'STRONG'

    def __repr__(self):
        return f'<TopicPerformance Topic {self.topic_id}: {self.accuracy_percentage}% ({self.classification})>'


class Recommendation(db.Model):
    __tablename__ = 'recommendations'
    id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey('test_attempts.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    classification = db.Column(db.String(20), nullable=False)         # 'WEAK', 'AVERAGE', 'STRONG'
    predicted_requirement = db.Column(db.String(50), nullable=False)  # 'Revision', 'Practice', 'Advanced Learning'
    recommendation_title = db.Column(db.String(200), nullable=False)
    recommendation_text = db.Column(db.Text, nullable=False)
    study_resources_json = db.Column(db.Text, nullable=True)          # JSON encoded resource list
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Recommendation Topic {self.topic_id}: {self.predicted_requirement}>'


class LearningResource(db.Model):
    __tablename__ = 'learning_resources'
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    provider = db.Column(db.String(100), nullable=False)  # e.g., 'GeeksforGeeks', 'YouTube', 'NPTEL', 'freeCodeCamp', 'Official Documentation'
    resource_type = db.Column(db.String(30), nullable=False)  # 'notes', 'video', 'documentation', 'practice'
    resource_url = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    language = db.Column(db.String(50), nullable=False, default='English')
    difficulty = db.Column(db.String(30), nullable=False, default='Beginner')  # 'Beginner', 'Intermediate', 'Advanced'
    verification_status = db.Column(db.String(20), nullable=False, default='verified')  # 'verified', 'unverified'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<LearningResource {self.id}: {self.title} ({self.provider}) [{self.resource_type}]>'
