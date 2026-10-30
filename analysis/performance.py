import pandas as pd
import numpy as np

def classify_accuracy(acc: float) -> str:
    """
    Classify topic performance based on strict criteria:
    Below 40%: WEAK
    40% to 70%: AVERAGE
    Above 70%: STRONG
    """
    if acc < 40.0:
        return 'WEAK'
    elif acc <= 70.0:
        return 'AVERAGE'
    else:
        return 'STRONG'


def analyze_attempt_responses(responses_data: list) -> dict:
    """
    Uses Pandas to process student test responses and compute metrics.
    
    responses_data: list of dicts with keys:
      - question_id
      - topic_id
      - topic_name
      - subject_id
      - subject_name
      - unit_number
      - difficulty
      - selected_answer
      - correct_answer
      - is_correct (bool)
      
    Returns dictionary with:
      - total_questions
      - total_correct
      - overall_score
      - subjects_df (as list of dicts)
      - topics_df (as list of dicts, sorted weakest first)
      - weak_topics (list)
      - average_topics (list)
      - strong_topics (list)
      - counts: {'weak': int, 'average': int, 'strong': int}
    """
    if not responses_data:
        return {
            'total_questions': 0,
            'total_correct': 0,
            'overall_score': 0.0,
            'subjects': [],
            'topics': [],
            'weak_topics': [],
            'average_topics': [],
            'strong_topics': [],
            'counts': {'weak': 0, 'average': 0, 'strong': 0}
        }

    # Build Pandas DataFrame
    df = pd.DataFrame(responses_data)

    # Ensure boolean/integer types
    df['is_correct_int'] = df['is_correct'].astype(int)

    total_questions = int(len(df))
    total_correct = int(df['is_correct_int'].sum())
    overall_score = round((total_correct / total_questions) * 100.0, 2) if total_questions > 0 else 0.0

    # 1. Subject-wise Analysis with Pandas groupby
    subject_group = df.groupby(['subject_id', 'subject_name']).agg(
        total_questions=('question_id', 'count'),
        correct_answers=('is_correct_int', 'sum')
    ).reset_index()

    subject_group['accuracy'] = (
        (subject_group['correct_answers'] / subject_group['total_questions']) * 100.0
    ).round(2)

    subjects_summary = subject_group.to_dict(orient='records')

    # 2. Topic-wise Analysis with Pandas groupby
    topic_group = df.groupby(['topic_id', 'topic_name', 'subject_name']).agg(
        total_questions=('question_id', 'count'),
        correct_answers=('is_correct_int', 'sum')
    ).reset_index()

    topic_group['accuracy'] = (
        (topic_group['correct_answers'] / topic_group['total_questions']) * 100.0
    ).round(2)

    # Topic Classification
    topic_group['classification'] = topic_group['accuracy'].apply(classify_accuracy)

    # Sort topics: Prioritize weakest topics first (ascending accuracy)
    topic_group = topic_group.sort_values(by=['accuracy', 'subject_name'], ascending=[True, True])

    topics_summary = topic_group.to_dict(orient='records')

    weak_topics = [t for t in topics_summary if t['classification'] == 'WEAK']
    average_topics = [t for t in topics_summary if t['classification'] == 'AVERAGE']
    strong_topics = [t for t in topics_summary if t['classification'] == 'STRONG']

    counts = {
        'weak': len(weak_topics),
        'average': len(average_topics),
        'strong': len(strong_topics)
    }

    return {
        'total_questions': total_questions,
        'total_correct': total_correct,
        'overall_score': overall_score,
        'subjects': subjects_summary,
        'topics': topics_summary,
        'weak_topics': weak_topics,
        'average_topics': average_topics,
        'strong_topics': strong_topics,
        'counts': counts
    }
