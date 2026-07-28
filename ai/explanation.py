"""
=========================================================
SentiVision AI
Explanation Generator Module

Developed by:
Emad Ali
UID: 24BSC10027
=========================================================
"""

from __future__ import annotations

from typing import List, Dict


class ExplanationGenerator:
    """
    Creates human-readable explanations
    from AI sentiment results.
    """

    def __init__(self):

        self.messages = {

            "POSITIVE":
                "The AI detected a positive emotional tone in the text.",

            "NEGATIVE":
                "The AI detected a negative emotional tone in the text.",

            "NEUTRAL":
                "The AI detected a neutral tone without strong positive or negative indicators."

        }


    # -------------------------------------------------
    # Generate Explanation
    # -------------------------------------------------

    def generate(
        self,
        sentiment: str,
        confidence: float,
        keywords: List[str]
    ) -> Dict:


        sentiment = sentiment.upper()


        message = self.messages.get(

            sentiment,

            "The AI could not determine the sentiment."

        )


        confidence_text = self.confidence_message(

            confidence

        )


        keyword_text = self.keyword_message(

            keywords

        )


        return {


            "summary": message,


            "confidence_message": confidence_text,


            "keyword_message": keyword_text,


            "full_explanation":

                f"{message} "
                f"{confidence_text} "
                f"{keyword_text}"


        }



    # -------------------------------------------------
    # Confidence Explanation
    # -------------------------------------------------

    def confidence_message(
        self,
        confidence: float
    ) -> str:


        if confidence >= 90:

            return (

                f"The prediction is highly confident "
                f"with {confidence}% confidence."

            )


        elif confidence >= 70:

            return (

                f"The prediction has moderate confidence "
                f"with {confidence}% confidence."

            )


        else:

            return (

                f"The prediction has lower confidence "
                f"with {confidence}% confidence."

            )



    # -------------------------------------------------
    # Keyword Explanation
    # -------------------------------------------------

    def keyword_message(
        self,
        keywords: List[str]
    ) -> str:


        if not keywords:

            return (

                "No important keywords were extracted."

            )


        return (

            "Important words detected: "

            + ", ".join(keywords)

            + "."

        )



    # -------------------------------------------------
    # Result Formatting
    # -------------------------------------------------

    def result_card(
        self,
        sentiment: str,
        confidence: float,
        keywords: List[str]
    ) -> Dict:


        result = self.generate(

            sentiment,

            confidence,

            keywords

        )


        return {


            "sentiment": sentiment,

            "confidence": confidence,

            "keywords": keywords,

            "explanation": result["full_explanation"]

        }



    # -------------------------------------------------
    # Information
    # -------------------------------------------------

    def information(self):

        return {


            "module": "Explanation Generator",

            "developer": "Emad Ali",

            "uid": "24BSC10027",

            "version": "1.0"

        }



# =====================================================
# Global Object
# =====================================================

explanation_generator = ExplanationGenerator()