# Vibeosys FastAPI Assignment

## Setup Instructions

1. Create MySQL database:
   CREATE DATABASE assignment_db;

2. Configure DB in `app/database.py` with your MySQL credentials.

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
uvicorn app.main:app --reload
```
