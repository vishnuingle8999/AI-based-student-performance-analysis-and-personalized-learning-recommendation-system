import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'ai-student-learning-rec-system-secret-key-2026')
    DATABASE_PATH = os.path.join(BASE_DIR, 'database', 'database.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    SYLLABUS_CSV = os.path.join(DATA_DIR, 'syllabus.csv')
    QUESTIONS_CSV = os.path.join(DATA_DIR, 'questions.csv')
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'data', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload
