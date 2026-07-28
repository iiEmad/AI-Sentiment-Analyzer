"""
=========================================================
SentiVision AI - Configuration File
Developed by: Emad Ali
UID: 24BSC10027
=========================================================
"""

from pathlib import Path
import os


class Config:
    """
    Main application configuration.
    """

    # --------------------------------------------------
    # Flask
    # --------------------------------------------------

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "SentiVision_AI_2026"
    )

    DEBUG = True

    # --------------------------------------------------
    # Project Paths
    # --------------------------------------------------

    BASE_DIR = Path(__file__).resolve().parent

    TEMPLATE_FOLDER = BASE_DIR / "templates"

    STATIC_FOLDER = BASE_DIR / "static"

    DATABASE_PATH = BASE_DIR / "sentiment_history.db"

    # --------------------------------------------------
    # AI Model
    # --------------------------------------------------

    MODEL_NAME = (
        "distilbert-base-uncased-finetuned-sst-2-english"
    )

    MAX_TEXT_LENGTH = 512

    # --------------------------------------------------
    # UI
    # --------------------------------------------------

    APP_NAME = "SentiVision AI"

    APP_VERSION = "3.0"

    DEVELOPER = "Emad Ali"

    UID = "24BSC10027"

    FOOTER = (
        "Developed by Emad Ali | UID: 24BSC10027"
    )

    # --------------------------------------------------
    # Dashboard
    # --------------------------------------------------

    MAX_HISTORY = 5000

    DEFAULT_CHART_COLOR = "#0d6efd"

    POSITIVE_COLOR = "#198754"

    NEGATIVE_COLOR = "#dc3545"

    NEUTRAL_COLOR = "#ffc107"

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    LOG_LEVEL = "INFO"

    # --------------------------------------------------
    # Miscellaneous
    # --------------------------------------------------

    DATE_FORMAT = "%d-%m-%Y %H:%M:%S"

    ENABLE_KEYWORDS = True

    ENABLE_EXPLANATION = True

    ENABLE_HISTORY = True

    ENABLE_DASHBOARD = True

    ENABLE_EMOTION = False