import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models.schema import (
    db, Student, Branch, Semester, Subject, Topic, Question, TestAttempt, LearningResource
)

def run_tests():
    print("==================================================")
    print("Running Automated Verification Suite for EduAI App")
    print("==================================================")

    with app.app_context():
        # 1. Verify Database Entities
        branch = Branch.query.filter_by(name="Artificial Intelligence & Data Science").first()
        assert branch is not None, "Branch AI&DS should exist"
        print(f"[PASS] Branch verified: {branch.name} ({branch.code})")

        sem5 = Semester.query.filter_by(branch_id=branch.id, name="Semester V").first()
        assert sem5 is not None, "Semester V should exist"
        print(f"[PASS] Semester verified: {sem5.name}")

        subjects_sem5 = Subject.query.filter_by(semester_id=sem5.id).all()
        assert len(subjects_sem5) == 5, f"Expected 5 DBATU core subjects for Semester V, found {len(subjects_sem5)}"
        print(f"[PASS] 5 DBATU subjects verified for Semester V:")
        for s in subjects_sem5:
            print(f"       - {s.name} ({s.code}) [{s.question_count} Qs]")

        total_subjects = Subject.query.count()
        assert total_subjects >= 17, f"Expected 17 subjects, found {total_subjects}"
        print(f"[PASS] Total DBATU subjects in database: {total_subjects}")

        total_questions = Question.query.count()
        assert total_questions >= 1020, f"Expected >= 1020 questions, found {total_questions}"
        print(f"[PASS] Total DBATU question bank items: {total_questions}")

        # Check curated learning resources
        total_resources = LearningResource.query.count()
        assert total_resources >= 80, f"Expected >= 80 curated resources, found {total_resources}"
        print(f"[PASS] Total Curated Educational Resources: {total_resources}")

        # Verify S001 student
        s001 = Student.query.filter_by(student_id="S001").first()
        assert s001 is not None, "Demo student S001 should exist"
        assert s001.check_password("password123"), "Password check for S001 failed"
        assert hasattr(s001, 'learning_preference'), "Student should have learning_preference attribute"
        print(f"[PASS] Demo student S001 verified (preference: {s001.learning_preference})")

        # Verify Admin account
        admin = Student.query.filter_by(email="admin@college.edu").first()
        assert admin is not None, "Admin account should exist"
        assert admin.role == 'admin', "Admin role mismatch"
        print(f"[PASS] Admin account verified (admin@college.edu)")

    # 2. Verify Flask Routes using Test Client
    client = app.test_client()

    # Index page
    res = client.get('/')
    assert res.status_code == 200, f"Index page returned {res.status_code}"
    assert b"AI-Based Personalized Student Learning Recommendation System" in res.data
    print("[PASS] Route GET / returned 200 OK")

    # Login demo student S001
    res = client.post('/login', data={
        'login_identifier': 'S001',
        'password': 'password123'
    }, follow_redirects=True)
    assert res.status_code == 200, f"Login returned {res.status_code}"
    assert b"Dashboard" in res.data
    print("[PASS] Route POST /login for S001 successful and redirected to Dashboard")

    # Syllabus page
    res = client.get('/syllabus')
    assert res.status_code == 200
    assert b"Machine Learning" in res.data
    print("[PASS] Route GET /syllabus returned 200 OK with Sem V subjects")

    # Diagnostic Test page
    res = client.get('/test')
    assert res.status_code == 200
    assert b"Comprehensive Diagnostic Test" in res.data
    print("[PASS] Route GET /test returned 200 OK with questions rendered")

    # Dashboard page
    res = client.get('/dashboard')
    assert res.status_code == 200
    assert b"Personalized Dashboard" in res.data
    assert b"subjectPerformanceChart" in res.data
    assert b"topicPerformanceChart" in res.data
    assert b"distributionDoughnutChart" in res.data
    assert b"progressComparisonChart" in res.data
    print("[PASS] Route GET /dashboard returned 200 OK with all 4 Chart.js charts")

    # Recommendations page
    res = client.get('/recommendations')
    assert res.status_code == 200
    assert b"Explainable AI Recommendation Engine" in res.data
    assert b"Your Learning Method Preference" in res.data
    assert b"Curated Learning Resources" in res.data
    assert b"Direct Topic Search Options" in res.data
    assert b"videoModal" in res.data
    print("[PASS] Route GET /recommendations returned 200 OK with ML rules and preferences")

    # Progress page
    res = client.get('/progress')
    assert res.status_code == 200
    assert b"Progress Tracking" in res.data
    print("[PASS] Route GET /progress returned 200 OK")

    # Update Learning Preference
    res = client.post('/preferences/update', data={'learning_preference': 'videos'}, follow_redirects=True)
    assert res.status_code == 200
    assert b"Video Lectures" in res.data
    print("[PASS] Route POST /preferences/update succeeded")

    # Reset back to both
    client.post('/preferences/update', data={'learning_preference': 'both'}, follow_redirects=True)

    # Admin Login
    with client.session_transaction() as sess:
        sess.clear()

    res = client.post('/login', data={
        'login_identifier': 'admin@college.edu',
        'password': 'admin123'
    }, follow_redirects=True)
    assert res.status_code == 200
    assert b"Administrator Portal" in res.data
    assert b"Curated Learning Resources Repository" in res.data
    print("[PASS] Route POST /login for Admin successful and redirected to Admin Portal")

    # Download sample CSVs
    res = client.get('/admin/sample-questions.csv')
    assert res.status_code == 200
    assert b"student_id,branch,year,semester" in res.data
    print("[PASS] Route GET /admin/sample-questions.csv verified")

    res = client.get('/admin/sample-syllabus.csv')
    assert res.status_code == 200
    assert b"branch,year,semester,subject,unit,topic,subtopic" in res.data
    print("[PASS] Route GET /admin/sample-syllabus.csv verified")

    print("==================================================")
    print("ALL TESTS PASSED SUCCESSFULLY! APPLICATION IS READY")
    print("==================================================")

if __name__ == '__main__':
    run_tests()
