import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    DATABASE = os.environ.get("DATABASE", os.path.join(BASE_DIR, "urls.db"))
    SHORT_CODE_LENGTH = int(os.environ.get("SHORT_CODE_LENGTH", 6))
    MAX_URL_LENGTH = 2048
    HOST = os.environ.get("HOST", "127.0.0.1")
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = os.environ.get("FLASK_DEBUG", "1") == "1"
