# Sarva Suvidhaen Assignment:  KPA Wheel Specifications API

A backend FastAPI service implementing two endpoints from the KPA Form Data API spec. This handles wheel-specification data with PostgreSQL, and supports submission and filtered retrieval:
1. GET /api/forms/wheel-specifications (GET with filters)
2. POST /api/forms/wheel-specifications


## Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Environment Management:** uv (with `.env`)
- **Schema Validation:** Pydantic



## Project Setup Instructions
### 1. Clone the repo and set up the environment
```bash
git clone https://github.com/yourusername/kpa-wheel-specs-api.git
cd kpa-wheel-specs-api
uv venv
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
uv pip install -r requirements.txt
```

### 3. Create a .env file in the root directory:
```.env
USERNAME=your_pg_user
PASSWORD=your_pg_password
HOSTNAME=localhost
PORT=5432
DBNAME=you_db_name
DATABASE_URL=postgresql://your_pg_user:your_pg_password@localhost:5432/kpa_wheel_spec_db
```

### 4. Set up PostgreSQL database & run Alembic migrations
```bash
CREATE DATABASE your_db_name
alembic upgrade head
```

### 5. Start the FastAPI server
```bash
uvicorn app.main:app --reload
```

### 6. Checkout APIs
- Got to http://localhost:8000/docs to use Swagger UI.





## Implemented APIs

### 1. GET /api/forms/wheel-specifications
- Retrieves wheel spec forms filtered by query parameters.
- Query Parameters (optional):
    - formNumber: string
    - submittedBy: string
    - submittedDate: string (YYYY-MM-DD)
- Response (sample):
```json
{
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "condemningDia": "825 (800-900)",
        "lastShopIssueSize": "837 (800-900)",
        "treadDiameterNew": "915 (900-1000)",
        "wheelGauge": "1600 (+2,-1)"
      }
    }
  ],
  "message": "Filtered wheel specification forms fetched successfully.",
  "success": true
}
```

### 2. POST /api/form/wheel-specifications
- Submits a new wheel specification form.
- Request Body (sample):
```json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "condemningDia": "825 (800-900)",
    "lastShopIssueSize": "837 (800-900)",
    "treadDiameterNew": "915 (900-1000)",
    "wheelGauge": "1600 (+2,-1)"
  }
}
```
- Response sample:
```json
{
  "data": {
    "formNumber": "WHEEL-2025-001",
    "status": "Saved",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03"
  },
  "message": "Wheel specification submitted successfully.",
  "success": true
}
```

##  Assumptions & Limitations
- Only formNumber, submittedBy, and submittedDate are filterable via GET.
- The formNumber must be unique — duplicates return a 400 error.
- Partial fields are allowed in the response (missing fields default to null).
- No authentication or file upload included (not part of chosen APIs).

## Project Structure
```bash
app/
├── main.py              # FastAPI app entry point
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
├── routes/              # API route definitions
├── database.py          # DB connection setup
├── config.py            # Loads environment from .env
alembic/                 # Alembic migration setup
```

## Demo Recording
- Link: https://drive.google.com/file/d/1pLDhxCSiRSDqi8Y2abICB-N4G9PVy3qy/view?usp=sharing

## Submission Details
- src code: https://github.com/BunnyEncoder20/sarva_suvidhaen_assignment
- postman collection (file include in root dir): varun_verma.postman_collection.json


## Built by
- Varun Verma
- Links:
    - [LinkedIn](https://www.linkedin.com/in/varun-verma-1547442a5/)
    - [Github](https://github.com/BunnyEncoder20)
    - [Portfolio Website](https://my-portfolio-3d-fawn.vercel.app/)
    - [DSA](https://takeuforward.org/plus/profile/BunnyEncoder)
