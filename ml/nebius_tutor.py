
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load API settings from the project's .env file
load_dotenv()

NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY")
NEBIUS_MODEL = os.getenv("NEBIUS_MODEL")

BASE_URL = "https://api.tokenfactory.nebius.com/v1/"


def generate_nebius_study_guidance(
    topic_name,
    subject_name,
    accuracy,
    classification,
    existing_plan
):
    """
    Generate personalised study guidance using Nebius AI.
    Existing ML recommendations remain unchanged.
    """

    if not NEBIUS_API_KEY or not NEBIUS_MODEL:
        return {
            "success": False,
            "guidance": "AI guidance is unavailable. Please follow the existing study plan."
        }

    try:
        client = OpenAI(
            base_url=BASE_URL,
            api_key=NEBIUS_API_KEY
        )

        prompt = f"""
You are a friendly tutor helping an engineering student.

Create simple and personalised study guidance.

Subject: {subject_name}
Topic: {topic_name}
Accuracy: {accuracy}%
Student classification: {classification}
Existing study plan: {existing_plan}

Return ONLY valid JSON with these keys:
{{
    "explanation": "Explain the student's learning situation in 2 sentences.",
    "study_strategy": "Give a practical study strategy.",
    "daily_task": "Give one small task the student can complete today.",
    "motivation": "Give one short encouraging sentence."
}}

Use simple English. Keep the response short and practical.
"""

        response = client.chat.completions.create(
            model=NEBIUS_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4,
            max_tokens=350
        )

        content = response.choices[0].message.content.strip()

        # Handle JSON enclosed in markdown code fences
        if content.startswith("```"):
            content = content.replace("```json", "", 1)
            content = content.replace("```", "").strip()

        guidance = json.loads(content)

        return {
            "success": True,
            "guidance": guidance
        }

    except Exception as e:
        print("Nebius AI guidance error:", str(e))

        return {
            "success": False,
            "guidance": "AI guidance is temporarily unavailable. Please follow the existing study plan."
        }
