import re
from urllib.parse import quote_plus

def extract_youtube_embed_url(url: str) -> str:
    """
    Extracts the YouTube embed URL from standard watch/short URLs.
    Example: https://www.youtube.com/watch?v=nk2CQITm_eo -> https://www.youtube-nocookie.com/embed/nk2CQITm_eo
    Returns empty string if not a YouTube URL.
    """
    if not url:
        return ""
    
    # Standard watch format: youtube.com/watch?v=VIDEO_ID
    match = re.search(r'(?:youtube\.com\/(?:watch\?v=|embed\/|v\/)|youtu\.be\/)([\w-]{11})', url)
    if match:
        video_id = match.group(1)
        return f"https://www.youtube-nocookie.com/embed/{video_id}"
    return ""


def score_resource(
    resource,
    student_preference: str,
    topic_accuracy: float,
    topic_name: str = "",
    subject_name: str = ""
) -> tuple[float, str]:
    """
    Computes an explainable ranking score and recommendation rationale for a learning resource.
    
    Factors considered:
    1. Student Learning Preference alignment ('notes', 'videos', 'both')
    2. Difficulty alignment relative to student's topic diagnostic accuracy:
       - WEAK (< 40%): beginner resources prioritized for fundamental revision
       - AVERAGE (40 - 70%): intermediate resources prioritized for concept drills
       - STRONG (> 70%): advanced resources prioritized for mastery & extension
    3. Platform Credibility & GeeksforGeeks suitability:
       - GeeksforGeeks receives a modest boost for notes and structured explanations (+6 pts)
       - High-quality video lectures from YouTube (freeCodeCamp, NPTEL, MIT, StatQuest) can rank higher
         when matching video preferences or visual demonstrations
    4. Verification status: verified resources (+20 pts)
    
    Returns:
        (score, explainable_reason)
    """
    score = 50.0  # Base score
    reasons = []

    res_type = (resource.resource_type or "").lower().strip()
    res_provider = (resource.provider or "").strip()
    res_difficulty = (resource.difficulty or "Beginner").capitalize().strip()
    is_verified = (resource.verification_status == 'verified')

    # 1. Verification status
    if is_verified:
        score += 20.0

    # 2. Student Learning Preference weighting
    pref = (student_preference or "both").lower().strip()
    
    if pref == "notes":
        if res_type in ["notes", "documentation"]:
            score += 35.0
            reasons.append("Matches your preference for written theory notes & code walkthroughs")
        elif res_type == "video":
            score += 10.0
            reasons.append("Available as a supplementary video lecture")
    elif pref == "videos":
        if res_type == "video":
            score += 35.0
            reasons.append("Matches your preference for video lectures with step-by-step visual demonstration")
        elif res_type in ["notes", "documentation"]:
            score += 10.0
            reasons.append("Available as a supplementary written reference")
    else:  # 'both'
        if res_type in ["notes", "documentation"]:
            score += 25.0
            reasons.append("Written explanation covering concepts & practical code")
        elif res_type == "video":
            score += 25.0
            reasons.append("Visual lecture demonstrating key concepts step-by-step")

    # 3. Diagnostic Accuracy & Difficulty Alignment
    if topic_accuracy < 40.0:
        # Student is WEAK: Needs clear, foundational beginner material
        if res_difficulty == "Beginner":
            score += 18.0
            reasons.append("Tailored for foundational revision (< 40% accuracy)")
        elif res_difficulty == "Intermediate":
            score += 8.0
        else:
            score -= 5.0
    elif topic_accuracy <= 70.0:
        # Student is AVERAGE: Ready for intermediate applied problem solving
        if res_difficulty == "Intermediate":
            score += 18.0
            reasons.append("Ideal for intermediate concept reinforcement (40-70% accuracy)")
        elif res_difficulty == "Beginner":
            score += 12.0
            reasons.append("Good for quick refresher of fundamental rules")
        else:
            score += 5.0
    else:
        # Student is STRONG (> 70%): Ready for advanced/deep-dive
        if res_difficulty == "Advanced":
            score += 18.0
            reasons.append("Advanced challenge for topic mastery (> 70% accuracy)")
        elif res_difficulty == "Intermediate":
            score += 10.0
        else:
            score += 5.0

    # 4. Educational Platform Credibility & GeeksforGeeks Consideration
    provider_lower = res_provider.lower()
    if "geeksforgeeks" in provider_lower:
        score += 6.0
        if "Comprehensive GeeksforGeeks article" not in " ".join(reasons):
            reasons.append("Structured GeeksforGeeks guide with definitions and code examples")
    elif "nptel" in provider_lower or "mit" in provider_lower or "stanford" in provider_lower:
        score += 7.0
        reasons.append(f"University curriculum lecture from {res_provider}")
    elif "freecodecamp" in provider_lower:
        score += 6.0
        reasons.append("In-depth tutorial from freeCodeCamp")
    elif "statquest" in provider_lower:
        score += 7.0
        reasons.append("Highly intuitive visual explanation from StatQuest")
    elif "official" in provider_lower or "documentation" in provider_lower or res_type == "documentation":
        score += 7.0
        reasons.append(f"Authoritative official documentation ({res_provider})")

    # Select primary concise explainable reason
    primary_reason = " · ".join(reasons[:2]) if reasons else "Recommended based on syllabus alignment"
    return score, primary_reason


def rank_resources_for_topic(
    resources: list,
    student_preference: str,
    topic_accuracy: float,
    topic_name: str = "",
    subject_name: str = ""
) -> list[dict]:
    """
    Ranks a list of LearningResource model objects or dicts according to
    student learning preference and performance context.
    """
    ranked_list = []
    
    for r in resources:
        # Handle both SQLAlchemy model instance and dictionary
        if hasattr(r, 'id'):
            res_id = r.id
            title = r.title
            provider = r.provider
            res_type = r.resource_type
            url = r.resource_url
            description = r.description or ""
            language = r.language or "English"
            difficulty = r.difficulty or "Beginner"
            status = r.verification_status or "verified"
        else:
            res_id = r.get('id', 0)
            title = r.get('title', '')
            provider = r.get('provider', '')
            res_type = r.get('resource_type', '')
            url = r.get('resource_url', '')
            description = r.get('description', '')
            language = r.get('language', 'English')
            difficulty = r.get('difficulty', 'Beginner')
            status = r.get('verification_status', 'verified')

        # Dummy object for scoring
        class DummyResource:
            pass
        d = DummyResource()
        d.resource_type = res_type
        d.provider = provider
        d.difficulty = difficulty
        d.verification_status = status

        score, reason = score_resource(d, student_preference, topic_accuracy, topic_name, subject_name)
        embed_url = extract_youtube_embed_url(url) if res_type == 'video' else ""

        ranked_list.append({
            "id": res_id,
            "title": title,
            "provider": provider,
            "resource_type": res_type,
            "resource_url": url,
            "embed_url": embed_url,
            "description": description,
            "language": language,
            "difficulty": difficulty,
            "verification_status": status,
            "ranking_score": round(score, 1),
            "recommendation_reason": reason,
            "is_fallback": False
        })

    # Sort descending by ranking score
    ranked_list.sort(key=lambda x: x["ranking_score"], reverse=True)
    return ranked_list


def generate_fallback_search_links(topic_name: str, subject_name: str = "", student_preference: str = "both") -> dict:
    """
    Generates intelligent, topic-specific educational search links when
    no verified resource is present in the database for a topic.
    Clearly labeled as search options without fabricating URLs.
    """
    clean_topic = topic_name.strip()
    query_str = f"{subject_name} {clean_topic}".strip() if subject_name else clean_topic
    encoded_query = quote_plus(query_str)
    encoded_topic = quote_plus(clean_topic)

    gfg_url = f"https://www.geeksforgeeks.org/search/?q={encoded_query}"
    yt_url = f"https://www.youtube.com/results?search_query={encoded_query}+lecture"
    nptel_url = f"https://www.google.com/search?q=site:nptel.ac.in+{encoded_query}"
    docs_url = f"https://www.google.com/search?q={encoded_query}+documentation"

    items = [
        {
            "id": f"search_gfg_{encoded_topic}",
            "title": f"Search GeeksforGeeks: {clean_topic}",
            "provider": "GeeksforGeeks",
            "resource_type": "notes",
            "resource_url": gfg_url,
            "embed_url": "",
            "description": f"Explore verified GeeksforGeeks articles, definitions, and code implementations for {clean_topic}.",
            "language": "English",
            "difficulty": "All Levels",
            "verification_status": "unverified",
            "ranking_score": 45.0,
            "recommendation_reason": "Topic-specific search fallback on GeeksforGeeks",
            "is_fallback": True
        },
        {
            "id": f"search_yt_{encoded_topic}",
            "title": f"Search YouTube Video Lectures: {clean_topic}",
            "provider": "YouTube",
            "resource_type": "video",
            "resource_url": yt_url,
            "embed_url": "",
            "description": f"Find video tutorials and recorded university lectures explaining {clean_topic}.",
            "language": "English",
            "difficulty": "All Levels",
            "verification_status": "unverified",
            "ranking_score": 45.0,
            "recommendation_reason": "Topic-specific video search fallback on YouTube",
            "is_fallback": True
        },
        {
            "id": f"search_nptel_{encoded_topic}",
            "title": f"Search NPTEL Course Materials: {clean_topic}",
            "provider": "NPTEL",
            "resource_type": "notes",
            "resource_url": nptel_url,
            "embed_url": "",
            "description": f"Search NPTEL IIT/IISc engineering curriculum lectures and slides for {clean_topic}.",
            "language": "English",
            "difficulty": "Intermediate",
            "verification_status": "unverified",
            "ranking_score": 42.0,
            "recommendation_reason": "NPTEL university curriculum search fallback",
            "is_fallback": True
        }
    ]

    # Adjust order of items based on student preference
    pref = (student_preference or "both").lower()
    if pref == "videos":
        items.sort(key=lambda x: 1 if x["resource_type"] == "video" else 2)
    elif pref == "notes":
        items.sort(key=lambda x: 1 if x["resource_type"] == "notes" else 2)

    return {
        "gfg_search": gfg_url,
        "youtube_search": yt_url,
        "nptel_search": nptel_url,
        "docs_search": docs_url,
        "items": items
    }
