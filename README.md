# AI-Based Personalized Student Learning Recommendation System

A comprehensive, production-ready web application built for the **Third Year B.Tech (Artificial Intelligence & Data Science)** mini project. The system diagnoses a student's conceptual strengths and weaknesses through semester-scoped diagnostic quizzes, analyzes performance using **Pandas**, and delivers explainable learning pathways using a **Scikit-learn Decision Tree Classifier** combined with a transparent pedagogical rule engine.

---

## Key Features

1. **Academic Scoping & Semester Selection**:
   - Dynamic hierarchy: `Branch` &rarr; `Academic Year` &rarr; `Semester` &rarr; `Subject` &rarr; `Unit` &rarr; `Topic` &rarr; `Question`.
   - **Crucial Boundary**: Loads **only** subjects and topics belonging strictly to the student's selected semester.
   - Pre-configured for: **Artificial Intelligence & Data Science**, **Third Year**, **Semester V** (extensible to all branches and years).

2. **Full Pre-Loaded Dataset (Sem V AI&DS)**:
   - **6 Subjects**:
     1. Data Analytics
     2. Artificial Intelligence
     3. Machine Learning
     4. Database Management Systems & NoSQL
     5. Deep Learning Basics
     6. Natural Language Processing Fundamentals
   - **18 Topics** (3 per subject).
   - **54 Diagnostic Questions** across Easy, Medium, and Hard difficulty levels.
   - Anonymous Student ID support (e.g. `S001`).

3. **Pandas Performance Analytics**:
   - Converts test attempt choices into structured DataFrames.
   - Computes:
     $$\text{Topic Accuracy (\%)} = \frac{\text{Correct Answers}}{\text{Total Attempted Questions}} \times 100$$
   - Strict classification thresholds:
     - **WEAK**: Accuracy $< 40\%$
     - **AVERAGE**: $40\% \le \text{Accuracy} \le 70\%$
     - **STRONG**: Accuracy $> 70\%$
   - Sorts topics **weakest first** for immediate triage.

4. **Dual-Layer Recommendation Engine (Scikit-Learn ML + Transparent Rules)**:
   - **Explainable Decision Tree Classifier** (`max_depth=3`) trained on student diagnostic vectors:
     - Features: `Topic Accuracy (%)`, `Previous Score (%)`, `Attempt Number`, `Correct Count`, `Total Questions`.
     - Target: `Revision`, `Practice`, or `Advanced Learning`.
   - **Pedagogical Rule Framework**:
     - **Weak Topics**: Basic concepts &rarr; Beginner learning material &rarr; Step-by-step examples &rarr; Practice questions &rarr; Revision quiz.
     - **Average Topics**: Concept revision &rarr; Intermediate examples &rarr; Practice questions &rarr; Topic quiz.
     - **Strong Topics**: Advanced questions &rarr; Higher difficulty problems &rarr; Additional learning material & research.
   - Curated reference documentation links for all 18 topics.

5. **Interactive Dashboard with 4 Chart.js Visualizations**:
   - **Subject-Wise Performance Bar Chart** (Color-coded: Red, Amber, Green).
   - **Topic-Wise Accuracy Horizontal Bar Chart** (Sorted weakest to strongest).
   - **Topic Classification Doughnut Chart** (Weak / Average / Strong distribution).
   - **Score Progression Chart** (Visual tracking across attempts).

6. **Progress Tracking & Re-Test Improvement**:
   - Take unlimited re-tests after studying recommended materials.
   - Compares:
     $$\text{Improvement} = \text{Current Score (\%)} - \text{Previous Score (\%)} \quad (\text{percentage points})$$
   - Historical attempt logs with before-and-after trajectory.

7. **Admin Portal & CSV Data Management**:
   - Upload new questions via 14-column CSV.
   - Upload new syllabus structures via CSV.
   - Manual GUI forms to add individual subjects, units, topics, and questions.
   - Download sample CSV templates directly from UI.
   - One-click "Reset & Re-Seed Demo Data" button for effortless viva resets.

---

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python Flask, Jinja2, Werkzeug |
| **Database & ORM** | SQLite, Flask-SQLAlchemy |
| **Data Analysis** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn (DecisionTreeClassifier) |
| **Charts** | Chart.js |
| **Frontend** | HTML5, CSS3, Bootstrap 5, Bootstrap Icons |

---

## Project Structure

```
AI Based Student Learning Recommendation System/
├── app.py                      # Flask routes, authentication, and test endpoints
├── config.py                   # App configurations (DB path, upload directories)
├── requirements.txt            # Dependencies (Flask, Pandas, Scikit-learn, etc.)
├── README.md                   # Complete documentation and viva defense guide
├── database/
│   ├── database.db             # SQLite database (auto-generated on launch)
│   └── db_init.py              # Schema creation, CSV importer, demo data seeder
├── data/
│   ├── syllabus.csv            # 6 subjects, units, 18 topics for Semester V
│   ├── questions.csv           # 54 diagnostic questions (Easy, Medium, Hard)
│   └── uploads/                # Directory for uploaded CSV datasets
├── models/
│   ├── __init__.py
│   └── schema.py               # SQLAlchemy ORM models
├── analysis/
│   ├── __init__.py
│   └── performance.py          # Pandas accuracy calculations & classification
├── ml/
│   ├── __init__.py
│   └── recommendation.py       # Scikit-learn Decision Tree model + rule engine
├── templates/
│   ├── base.html               # Shared layout, navbar, semester badge, alerts
│   ├── index.html              # Landing page & workflow visualization
│   ├── login.html              # Student / Admin login with demo quick fills
│   ├── register.html           # Student registration with branch/semester pickers
│   ├── profile.html            # Profile & semester scope switcher
│   ├── syllabus.html           # Semester syllabus viewer with interactive accordions
│   ├── test.html               # Timed diagnostic test with question jump palette
│   ├── result.html             # Score breakdown, subject stats, and topic tags
│   ├── dashboard.html          # Student dashboard with 4 Chart.js charts
│   ├── recommendations.html    # AI learning recommendations sorted weakest first
│   ├── progress.html           # Re-test comparison & improvement percentage points
│   └── admin.html              # Admin CSV uploader and question bank manager
├── static/
│   ├── css/
│   │   └── style.css           # Modern clean academic portal styling
│   └── js/
│       └── dashboard_charts.js # Chart.js renderers
└── tests/
    └── verify_app.py           # Automated test suite
```

---

## Installation & Setup Instructions

### 1. Prerequisites
- Python 3.10, 3.11, 3.12, 3.13, or 3.14 installed.

### 2. Clone or Open Project
Open a terminal in the project directory:
```bash
cd "AI Based Student Learning Recommendation System"
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
The console will display:
```
Database initialized successfully.
Starting AI-Based Personalized Student Learning Recommendation System...
 * Running on http://127.0.0.1:5000
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## Pre-Configured Demo Accounts (For Viva Presentation)

The database automatically initializes on first run with demo accounts pre-loaded:

### 1. Student Account (With Pre-Analyzed Baseline Attempt)
- **Login Identifier**: `S001` or `s001@college.edu`
- **Password**: `password123`
- **Role**: Student (Artificial Intelligence & Data Science, Third Year, Semester V)
- **Features**: Immediate access to Dashboard showing 4 Chart.js charts, identified weak topics, and personalized recommendations.

### 2. Administrator Account
- **Login Identifier**: `admin@college.edu`
- **Password**: `admin123`
- **Role**: Administrator
- **Features**: Upload CSV question banks, import new syllabus CSVs, inspect student logs, and reset demo data.

---

## CSV Dataset Specifications

### 1. Questions CSV Format (`data/questions.csv`)
Must contain the following 14 columns:
```csv
student_id,branch,year,semester,subject,unit,topic,question,option_a,option_b,option_c,option_d,correct_answer,difficulty
```
- `correct_answer`: Must be `A`, `B`, `C`, or `D`.
- `difficulty`: `Easy`, `Medium`, or `Hard`.

### 2. Syllabus CSV Format (`data/syllabus.csv`)
Must contain the following 7 columns:
```csv
branch,year,semester,subject,unit,topic,subtopic
```
- `subtopic`: Semicolon-separated list (e.g. `Series; DataFrames; GroupBy`).

---

## Typical User Flow

```
Login as S001 (or Register)
       │
       ▼
Select Branch (AI & DS) ──> Year (Third Year) ──> Semester (Semester V)
       │
       ▼
View Semester Syllabus (Strictly 6 Semester V subjects loaded)
       │
       ▼
Take Diagnostic Test (54 Questions: Easy, Medium, Hard)
       │
       ▼
Pandas Evaluates Accuracy (<40% WEAK, 40-70% AVERAGE, >70% STRONG)
       │
       ▼
Scikit-learn Model Predicts Learning Path (Revision / Practice / Advanced)
       │
       ▼
Personalized Dashboard Displays 4 Interactive Chart.js Visualizations
       │
       ▼
Study Weakest Topics First via Step-by-Step Recommendations
       │
       ▼
Take Re-Test Assessment
       │
       ▼
Progress Page Plots Score Trajectory & Computes Improvement (+X%)
```

---

## College Viva Preparation Guide (Q & A)

### Q1: Why did you use Pandas in this system?
**Answer**:
> "Pandas provides high-performance, vectorized aggregation operations. When a student completes a 54-question diagnostic test, all responses are converted into a Pandas DataFrame. Using `df.groupby(['topic_id', 'topic_name'])`, we instantaneously calculate topic accuracy, filter counts of correct answers, and apply vectorized classification logic into WEAK, AVERAGE, and STRONG categories without writing slow procedural nested loops."

### Q2: What Machine Learning model is used, and why did you choose it?
**Answer**:
> "We used a **Decision Tree Classifier** from **Scikit-learn** (`sklearn.tree.DecisionTreeClassifier`). In educational recommender systems, explainability and transparency are paramount. Black-box models like deep neural networks cannot clearly explain *why* a student was assigned a particular remedial path. A Decision Tree evaluates student features (`topic_accuracy`, `previous_score`, `attempt_number`, `correct_count`) along explicit threshold branches (e.g., accuracy $\le 40\% \to \text{Revision}$) and produces clear feature importances, ensuring the system can be defended and trusted by educators."

### Q3: How do you prevent students from seeing subjects from other semesters?
**Answer**:
> "The database schema enforces a strict relational hierarchy: `Branch` $\to$ `Year` $\to$ `Semester` $\to$ `Subject` $\to$ `Unit` $\to$ `Topic` $\to$ `Question`. Every subject has a foreign key `semester_id`. When querying the syllabus or generating a diagnostic test, the backend filters strictly using `Subject.semester_id == current_semester.id`. This ensures complete academic isolation between semesters."

### Q4: How is student improvement calculated during re-tests?
**Answer**:
> "Each assessment is persisted in the `test_attempts` table with an incremented `attempt_number` and timestamp. The Progress module computes the difference in percentage points between the current re-test score and the student's previous baseline score: $\text{Improvement} = \text{Score}_{\text{current}} - \text{Score}_{\text{previous}}$. Both attempts are rendered side-by-side graphically using Chart.js."

### Q5: How does the system prioritize recommendations?
**Answer**:
> "The recommendation engine sorts topic records in ascending order of accuracy ($\text{accuracy} \uparrow$). As a result, the student's most critically deficient topics ($< 40\%$) appear at the very top of the recommendation page with foundational revision steps, before moving on to average or strong topics."
