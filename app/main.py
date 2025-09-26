"""
main.py: FastAPI application entry point for Video Recommendation System.
"""

from fastapi import FastAPI, HTTPException
from app import db, recommender

app = FastAPI(
    title="AI Video Recommendation API",
    description="Personalized video recommendations using FastAPI."
)

@app.get("/")
def read_root():
    """
    Root endpoint with a welcome message.
    """
    return {"message": "Welcome to AI Video Recommendation!"}

@app.on_event("startup")
def startup():
    """
    Initializes the demo database on startup.
    """
    db.init_db()

@app.get("/init_demo")
def init_demo():
    """
    Populates the demo database with test users, videos, and interactions.
    """
    db.insert_demo_data()
    return {"message": "Demo data inserted"}

@app.get("/feed")
def get_feed(username: str, project_code: str = None):
    """
    Returns personalized or category-specific video recommendations for a user.
    """
    try:
        return recommender.get_recommendations(username, project_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
