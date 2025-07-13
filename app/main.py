from fastapi import FastAPI, status

# routes import
from app.routes import wheel_specs as wheel_specification_routes

# database import
# from app.database import Base, engine

# CORS middleware
from fastapi.middleware.cors import CORSMiddleware


'''------------------------------------------------------------------'''


# making FastAPI class instance
app = FastAPI()

# lists of alllowed origins that can reach out backend
allowed_orgins = ['*']

# Adding the CORS middleware to our app
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_orgins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Commented out because Alembic took over to making PgSQL tables
# Making connection to Postgres DB using SLQ Alchemy. reMakes the tables on app startup
# Base.metadata.create_all(bind=engine)


# Root route
@app.get("/")
async def root():
    return {"status_code": status.HTTP_200_OK , "msg": "Hello Sarva Suvidhaen"}



# include routers
app.include_router(wheel_specification_routes.router)
