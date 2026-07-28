"""
=========================================================
SentiVision AI
Keyword Extraction Module

Developed by:
Emad Ali
UID: 24BSC10027
=========================================================
"""

from __future__ import annotations

import re
from typing import List


class KeywordExtractor:
    """
    Extracts meaningful keywords from text.
    """


    def __init__(self) -> None:

        self.stop_words = {

            "a", "an", "the",

            "this", "that", "these", "those",

            "is", "am", "are", "was", "were",

            "be", "been", "being",

            "have", "has", "had",

            "do", "does", "did",

            "can", "could", "shall",

            "should", "will", "would",

            "may", "might", "must",

            "and", "or", "but",

            "if", "then", "than",

            "because", "while",

            "with", "without",

            "from", "into", "onto",

            "about", "above", "below",

            "after", "before",

            "very", "really", "quite",

            "just", "only", "also",

            "there", "their", "them",

            "they", "your", "ours",

            "ourselves", "myself",

            "his", "her", "hers",

            "its", "it's"

        }


    # --------------------------------------------------
    # Public Method
    # --------------------------------------------------

    def extract(
        self,
        text: str,
        max_keywords: int = 10
    ) -> List[str]:

        text = self.clean(text)

        words = re.findall(
            r"[A-Za-z]+",
            text.lower()
        )

        keywords = []

        for word in words:

            if len(word) < 4:
                continue

            if word in self.stop_words:
                continue

            if word.isdigit():
                continue

            if word not in keywords:

                keywords.append(word)

        return keywords[:max_keywords]


    # --------------------------------------------------
    # Cleaning
    # --------------------------------------------------

    def clean(
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
    # Frequency
    # --------------------------------------------------

    def frequency(
        self,
        text: str
    ) -> dict:

        keywords = self.extract(
            text,
            max_keywords=1000
        )

        frequency = {}

        for word in keywords:

            frequency[word] = (

                frequency.get(word, 0)

                + 1

            )

        return dict(

            sorted(

                frequency.items(),

                key=lambda item: item[1],

                reverse=True

            )

        )


    # --------------------------------------------------
    # Count
    # --------------------------------------------------

    def count(
        self,
        text: str
    ) -> int:

        return len(

            self.extract(text)

        )


    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def information(self) -> dict:

        return {

            "module": "Keyword Extractor",

            "version": "1.0",

            "developer": "Emad Ali",

            "uid": "24BSC10027"

        }


# =====================================================
# Singleton Object
# =====================================================

keyword_extractor = KeywordExtractor()