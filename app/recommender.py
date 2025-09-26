"""
recommender.py: Contains recommendation logic for the video recommendation system.
"""

from app import db

def get_recommendations(username, project_code=None):
    """
    Returns personalized video recommendations for a user.
    If project_code is provided, recommendations are filtered by category.
    """
    if username not in db.users:
        raise Exception("User not found")

    # Videos already watched by the user
    watched = {i["video_id"] for i in db.interactions if i["user"] == username}

    # Recommend unwatched videos, optionally filtered by category
    recs = []
    for vid, info in db.videos.items():
        if vid not in watched:
            if project_code and info["category"] != project_code:
                continue
            recs.append({"video_id": vid, "title": info["title"], "category": info["category"]})

    return {"user": username, "recommendations": recs}
