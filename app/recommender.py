from app import db

def get_recommendations(username, project_code=None):
    if username not in db.users:
        raise Exception("User not found")

    # Get videos the user already watched
    watched = {i["video_id"] for i in db.interactions if i["user"] == username}

    # Simple recommendation: suggest unwatched videos
    recs = []
    for vid, info in db.videos.items():
        if vid not in watched:
            if project_code and info["category"] != project_code:
                continue
            recs.append({"video_id": vid, "title": info["title"], "category": info["category"]})

    return {"user": username, "recommendations": recs}
