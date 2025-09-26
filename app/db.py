"""
db.py: Simple in-memory demo database for users, videos, and user interactions.
"""

users = {}
videos = {}
interactions = []

def init_db():
    """
    Initializes the in-memory database (for demo purpose).
    """
    global users, videos, interactions
    users = {}
    videos = {}
    interactions = []

def insert_demo_data():
    """
    Inserts sample demo data for users, videos, and interactions.
    """
    global users, videos, interactions
    users = {"rohit": {}, "alice": {}, "bob": {}}
    videos = {
        1: {"title": "Intro to AI", "category": "tech"},
        2: {"title": "Funny Cats", "category": "fun"},
        3: {"title": "Space Documentary", "category": "science"},
        4: {"title": "Python Tutorial", "category": "tech"}
    }
    interactions = [
        {"user": "rohit", "video_id": 1},
        {"user": "rohit", "video_id": 4},
        {"user": "alice", "video_id": 2},
        {"user": "bob", "video_id": 3},
    ]
