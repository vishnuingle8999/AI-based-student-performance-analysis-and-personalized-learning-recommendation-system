import os
import sys
import sqlite3

def run_migration():
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    print(f"Connecting to database at {db_path}...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check columns of students table
    cursor.execute("PRAGMA table_info(students)")
    columns = [row[1] for row in cursor.fetchall()]
    print("Existing columns in students:", columns)

    if 'learning_preference' not in columns:
        cursor.execute("ALTER TABLE students ADD COLUMN learning_preference VARCHAR(20) DEFAULT 'both'")
        conn.commit()
        print("[SUCCESS] Added learning_preference column to students table.")
    else:
        print("[INFO] learning_preference column already exists.")

    # Ensure existing rows have 'both'
    cursor.execute("UPDATE students SET learning_preference = 'both' WHERE learning_preference IS NULL")
    conn.commit()

    cursor.execute("SELECT id, student_id, name, role, learning_preference FROM students")
    for row in cursor.fetchall():
        print(f"  Student {row[1]} ({row[2]}): Role={row[3]}, Preference={row[4]}")

    conn.close()

    # Now import app safely and create new tables such as learning_resources
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from app import app
    from models.schema import db, Student, Subject, Question, LearningResource

    with app.app_context():
        db.create_all()
        print("[SUCCESS] db.create_all() executed.")
        print("  Students count:", Student.query.count())
        print("  Subjects count:", Subject.query.count())
        print("  Questions count:", Question.query.count())
        print("  LearningResources count:", LearningResource.query.count())

if __name__ == '__main__':
    run_migration()
