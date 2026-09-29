from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Medical Guidance System"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str
    
    # Security / JWT
    SECRET_KEY: str = "medical-guidance-super-secret-key-change-in-production-2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # File uploads & Storage
    UPLOAD_DIR: str = "uploads"
    STORAGE_BACKEND: str = "auto"  # 'auto', 's3', or 'local'
    S3_BUCKET_NAME: str | None = None
    AWS_REGION: str = "us-east-1"
    AWS_ACCESS_KEY_ID: str | None = None
    AWS_SECRET_ACCESS_KEY: str | None = None
    S3_CUSTOM_DOMAIN: str | None = None  # e.g., CloudFront CDN domain: d1234.cloudfront.net

    # Serverless & Database Behavior
    AUTO_SEED_ON_STARTUP: bool = True

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()