import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from mangum import Mangum

from app.core.config import settings
from app.db.database import SessionLocal
from app.db.seed import seed_database
from app.routers.api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: ensure upload folder if running with local storage
    if not settings.S3_BUCKET_NAME:
        try:
            os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
        except OSError:
            pass  # Read-only filesystem in some Lambda configurations

    # Seed default roles/permissions if enabled (disable in scaled serverless)
    if settings.AUTO_SEED_ON_STARTUP:
        db = SessionLocal()
        try:
            seed_database(db)
        except Exception as e:
            print(f"Database seed note: {e}")
        finally:
            db.close()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static file serving for uploads (when local directory exists)
if os.path.exists(settings.UPLOAD_DIR):
    app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")

# Include all API v1 endpoints
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/", tags=["Health"])
def root():
    return {
        "status": "online",
        "message": f"Welcome to {settings.PROJECT_NAME} Backend API",
        "docs_url": "/docs",
        "api_v1": settings.API_V1_STR,
        "runtime": "AWS Lambda / Serverless Ready" if os.environ.get("AWS_LAMBDA_FUNCTION_NAME") else "Standard ASGI",
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "database": "connected",
        "storage": "AWS S3" if settings.S3_BUCKET_NAME else "Local Disk",
        "is_lambda": bool(os.environ.get("AWS_LAMBDA_FUNCTION_NAME")),
    }


# AWS Lambda ASGI handler adapter
# lifespan="off" avoids re-running startup/shutdown lifecycle logic on every single invocation
handler = Mangum(app, lifespan="off")
