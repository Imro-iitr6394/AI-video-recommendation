from fastapi import FastAPI, HTTPException
from app import db, recommender

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init_db()

@app.post("/init_demo")
def init_demo():
    db.insert_demo_data()
    return {"message": "Demo data inserted"}

@app.get("/feed")
def get_feed(username: str, project_code: str = None):
    try:
        return recommender.get_recommendations(username, project_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
