import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "aurora_secret_key")

    # SQLite DB داخل مجلد المشروع
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "aurora.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "aurora-secret-key")
    SQLALCHEMY_DATABASE_URI = "sqlite:///aurora.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
