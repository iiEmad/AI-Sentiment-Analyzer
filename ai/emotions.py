"""
=========================================================
SentiVision AI
Emotion Analysis Module

Developed by:
Emad Ali
UID: 24BSC10027
=========================================================
"""

from __future__ import annotations

import re
import logging
from typing import Dict

from transformers import pipeline


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class EmotionAnalyzer:
    """
    Emotion Analysis Engine.

    This module is intentionally separated from the
    sentiment analyzer to keep the project modular.
    """

    def __init__(self) -> None:

        logging.info("Loading emotion model...")

        self.model = pipeline(
            task="text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )

        logging.info("Emotion model loaded successfully.")

    # --------------------------------------------------
    # Public Method
    # --------------------------------------------------

    def analyze(self, text: str) -> Dict:

        cleaned_text = self.clean_text(text)

        predictions = self.model(cleaned_text)[0]

        predictions.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        best = predictions[0]

        return {

            "emotion": best["label"].upper(),

            "confidence": round(
                best["score"] * 100,
                2
            ),

            "all_predictions": [

                {
                    "emotion": item["label"].upper(),
                    "confidence": round(
                        item["score"] * 100,
                        2
                    )
                }

                for item in predictions

            ]

        }

    # --------------------------------------------------
    # Cleaning
    # --------------------------------------------------

    def clean_text(
        self,
        text: str
    ) -> str:

        text = text.strip()

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    def validate(
        self,
        text: str
    ) -> bool:

        return bool(text.strip())

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def information(self) -> Dict:

        return {

            "module": "Emotion Analyzer",

            "developer": "Emad Ali",

            "uid": "24BSC10027",

            "status": "Ready"

        }


emotion_analyzer = EmotionAnalyzer()