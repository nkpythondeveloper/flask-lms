import os


def env_bool(key: str, default: str = "false") -> bool:
    """ Read an environment variable as a boolean. """
    return os.getenv(key, default).strip().lower() in {"1", "true", "yes", "on"}


def env_int(key: str, default: int) -> int:
    """ Read an environment variable as an int with fallback. """
    try:
        return int(os.getenv(key, default))
    except (TypeError, ValueError):
        return default


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = env_bool("FLASK_DEBUG", "true")
    TIMEZONE = os.getenv("TZ", "Asia/Kolkata")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://lms.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 1800, # 30 mins
    }

    MAIL_SERVER = os.getenv("MAIL_SERVER", )
    MAIL_PORT = env_int("MAIL_PORT", 587)
    MAIL_USE_TLS = env_bool("MAIL_USE_TLS", "true")
    MAIL_USE_SSL = env_bool("MAIL_USE_SSL", "false")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", "noreply@lms.local")

    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1")
    CELERY_TASK_IGNORE_RESULT = env_bool("CELERY_TASK_IGNORE_RESULT", "true")
    CELERY_WORKER_PREFETCH_MULTIPLIER = env_int("CELERY_WORKER_PREFETCH_MULTIPLIER", 1)
    CELERY_TIMEZONE = TIMEZONE

    SESSION_COOKIE_SECURE = env_bool("SESSION_COOKIE_SECURE", "false")
    REMEMBER_COOKIE_SECURE = env_bool("REMEMBER_COOKIE_SECURE", "false")


class DevConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True


class TestConfig(BaseConfig):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    CELERY_TASK_ALWAYS_EAGER = True  # Run Celery tasks inline during tests