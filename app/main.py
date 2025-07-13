from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

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

# FastAPI built in Exception handler override
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "message": "Validation failed. Please check the input format.",
            "errors": exc.errors()
        },
    )

# Root route
@app.get("/")
async def root():
    return {"status_code": status.HTTP_200_OK , "msg": "Hello Sarva Suvidhaen"}



# include routers
app.include_router(wheel_specification_routes.router)
