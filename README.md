# AI Video Recommendation System

## Introduction

Hi, I'm Rohit Yadav. This repository contains my submission for the Video Recommendation Assignment. I have built a backend API that provides personalized video recommendations using FastAPI. The project demonstrates key concepts like recommendation algorithms, handling cold start problems, integration with external APIs, and is ready for deployment.

---

## Features

- **Personalized Video Feed:** Returns tailored recommendations for each user.
- **Category-based Feed:** Allows filtering recommendations by project code (category/mood).
- **Demo Data Initialization:** Easily populate the database with test users and videos.
- **Swagger/OpenAPI Docs:** Interactive API docs at `/docs`.
- **Ready for External API Integration:** Uses environment variables for secure access.
- **Database Migrations:** Alembic migration-ready.
- **Efficient Data Handling:** Uses in-memory DB for demo, extensible to real DB.

---

## Technology Stack

- **Backend Framework:** FastAPI
- **Database:** In-memory (demo); supports Alembic for migrations
- **Documentation:** Swagger/OpenAPI (`/docs`)
- **API Testing:** Postman Collection included

---

## Prerequisites

- Python 3.8+
- (Recommended) Virtual environment

---

## Getting Started

### 1. **Clone the Repository**

```bash
git clone https://github.com/Imro-iitr6394/video-recommendation-engine.git
cd video-recommendation-engine
```

### 2. **Set Up Virtual Environment**

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Configure Environment Variables**

Set the following in Render dashboard or in a `.env` file for local testing:

```
FLIC_TOKEN=your_flic_token
API_BASE_URL=https://api.socialverseapp.com
```

### 5. **Run Database Migrations** (if using a real DB)

```bash
alembic upgrade head
```

### 6. **Start the Server**

```bash
uvicorn app.main:app --reload
```

---

## API Endpoints

| Endpoint                                 | Method | Description                                   |
|-------------------------------------------|--------|-----------------------------------------------|
| `/`                                      | GET    | Welcome message                               |
| `/init_demo`                             | POST   | Populate demo data                            |
| `/feed?username={username}`              | GET    | Personalized recommendations for a user       |
| `/feed?username={username}&project_code={project_code}` | GET | Category/mood-specific recommendations        |

Swagger docs available at `/docs` (e.g., [http://localhost:8000/docs](http://localhost:8000/docs) or your Render URL).

---

## How to Test

1. **Import the included Postman Collection** (`Video-Recommendation.postman_collection.json`) into Postman.
2. **Initialize demo data** by sending a POST to `/init_demo`.
3. **Get recommendations** by sending a GET to `/feed?username=rohit` or `/feed?username=rohit&project_code=tech`.
4. **Try out endpoints interactively** using Swagger UI at `/docs`.

---

## System Overview

Detailed explanation of the recommendation algorithm and design decisions is available in [`docs/system_overview.md`](docs/system_overview.md).

---




