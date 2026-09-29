import os
import shutil
import logging
from typing import BinaryIO
from fastapi import UploadFile
from app.core.config import settings

logger = logging.getLogger(__name__)

# Lazy import boto3 so local development doesn't fail if AWS is not needed
_s3_client = None


def get_s3_client():
    global _s3_client
    if _s3_client is None:
        import boto3
        kwargs = {"region_name": settings.AWS_REGION}
        if settings.AWS_ACCESS_KEY_ID and settings.AWS_SECRET_ACCESS_KEY:
            kwargs["aws_access_key_id"] = settings.AWS_ACCESS_KEY_ID
            kwargs["aws_secret_access_key"] = settings.AWS_SECRET_ACCESS_KEY
        _s3_client = boto3.client("s3", **kwargs)
    return _s3_client


class StorageService:
    """
    Unified Storage Service supporting:
    1. AWS S3 (Serverless production / cloud deployment)
    2. Local Disk (Development / fallback)
    """

    @classmethod
    def is_s3_enabled(cls) -> bool:
        if settings.STORAGE_BACKEND == "local":
            return False
        if settings.STORAGE_BACKEND == "s3":
            return True
        return bool(settings.S3_BUCKET_NAME)

    @classmethod
    def save_file(
        cls,
        file: UploadFile,
        target_filename: str,
        folder_prefix: str = "",
    ) -> str:
        """
        Saves an uploaded file either to AWS S3 or the local file system.
        Returns the accessible file URL.
        """
        content_type = file.content_type or "application/octet-stream"

        if cls.is_s3_enabled():
            return cls._save_to_s3(
                file_obj=file.file,
                filename=target_filename,
                folder_prefix=folder_prefix,
                content_type=content_type,
            )
        else:
            return cls._save_to_local(
                file_obj=file.file,
                filename=target_filename,
                folder_prefix=folder_prefix,
            )

    @classmethod
    def _save_to_s3(
        cls,
        file_obj: BinaryIO,
        filename: str,
        folder_prefix: str,
        content_type: str,
    ) -> str:
        s3 = get_s3_client()
        s3_key = f"{folder_prefix.strip('/')}/{filename}" if folder_prefix else filename
        extra_args = {"ContentType": content_type}

        logger.info(f"Uploading file {filename} to S3 bucket {settings.S3_BUCKET_NAME} key {s3_key}")
        file_obj.seek(0)
        s3.upload_fileobj(
            file_obj,
            settings.S3_BUCKET_NAME,
            s3_key,
            ExtraArgs=extra_args,
        )

        if settings.S3_CUSTOM_DOMAIN:
            return f"https://{settings.S3_CUSTOM_DOMAIN}/{s3_key}"
        return f"https://{settings.S3_BUCKET_NAME}.s3.{settings.AWS_REGION}.amazonaws.com/{s3_key}"

    @classmethod
    def _save_to_local(
        cls,
        file_obj: BinaryIO,
        filename: str,
        folder_prefix: str,
    ) -> str:
        target_dir = os.path.join(settings.UPLOAD_DIR, folder_prefix) if folder_prefix else settings.UPLOAD_DIR
        os.makedirs(target_dir, exist_ok=True)
        file_path = os.path.join(target_dir, filename)

        file_obj.seek(0)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file_obj, buffer)

        logger.info(f"Saved file to local path: {file_path}")
        if folder_prefix:
            return f"/uploads/{folder_prefix.strip('/')}/{filename}"
        return f"/uploads/{filename}"

    @classmethod
    def delete_file(cls, file_url_or_key: str) -> bool:
        """
        Deletes a file from either S3 or local storage based on current mode and URL format.
        """
        if not file_url_or_key:
            return False

        try:
            if cls.is_s3_enabled() and ("amazonaws.com" in file_url_or_key or settings.S3_CUSTOM_DOMAIN in file_url_or_key if settings.S3_CUSTOM_DOMAIN else False):
                s3 = get_s3_client()
                # Extract key from URL
                key = file_url_or_key.split(".amazonaws.com/")[-1] if ".amazonaws.com/" in file_url_or_key else file_url_or_key.split(f"{settings.S3_CUSTOM_DOMAIN}/")[-1]
                s3.delete_object(Bucket=settings.S3_BUCKET_NAME, Key=key)
                return True
            elif file_url_or_key.startswith("/uploads/"):
                relative_path = file_url_or_key.replace("/uploads/", "", 1)
                full_path = os.path.join(settings.UPLOAD_DIR, relative_path)
                if os.path.exists(full_path):
                    os.remove(full_path)
                    return True
        except Exception as e:
            logger.error(f"Failed to delete file {file_url_or_key}: {e}")
            return False
        return False
