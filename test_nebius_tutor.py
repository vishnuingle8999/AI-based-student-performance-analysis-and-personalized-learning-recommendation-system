
from ml.nebius_tutor import generate_nebius_study_guidance

result = generate_nebius_study_guidance(
    topic_name="Python Functions",
    subject_name="Python Programming",
    accuracy=45,
    classification="WEAK",
    existing_plan="Revise function syntax and practise basic function programs."
)

print("\nNebius AI Test Result:")
print(result)
