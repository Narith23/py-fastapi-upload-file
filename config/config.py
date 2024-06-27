import os

APP_NAME = "Upload File FastAPI"
APP_DESCRIPTION = "Upload File FastAPI"
APP_VERSION = "1.0.0"

IMAGE_FOLDER = "D:/python project/GitHub/py-fastapi-upload-file/uploads"

MONGO_URL = os.getenv("MONGO_URL", "mongodb://127.0.0.1:27017")
MONGO_DATABASE = os.getenv("MONGO_DATABASE", "py-fastapi-upload-file")
