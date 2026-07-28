"""
=========================================================
SentiVision AI
Advanced Sentiment Analysis Engine

Developed by:
Emad Ali
UID: 24BSC10027
=========================================================
"""

import logging
from transformers import pipeline


class SentimentAnalyzer:
    """
    Advanced NLP Sentiment Analyzer
    Using Hugging Face Transformer Models
    """

    def __init__(self):

        self.model_name = (
            "distilbert-base-uncased-finetuned-sst-2-english"
        )

        logging.info(
            "Loading sentiment AI model..."
        )


        try:

            self.classifier = pipeline(

                task="sentiment-analysis",

                model=self.model_name,

                truncation=True,

                max_length=512

            )


            logging.info(
                "Sentiment model loaded successfully."
            )


        except Exception as error:

            logging.error(
                f"Model loading failed: {error}"
            )

            self.classifier = None



    # =====================================
    # Main Prediction Function
    # =====================================

    def predict(self, text):


        if not text or not text.strip():

            return {

                "label": "NEUTRAL",

                "confidence": 0.0

            }



        if self.classifier is None:

            return {

                "label": "NEUTRAL",

                "confidence": 0.0

            }



        try:


            result = self.classifier(

                text.strip()

            )[0]


            label = result["label"].upper()


            score = result["score"] * 100



            return {


                "label": label,


                "confidence":
                    round(score, 2)


            }



        except Exception as error:


            logging.error(

                f"Prediction error: {error}"

            )


            return {


                "label": "NEUTRAL",

                "confidence": 0.0


            }




    # =====================================
    # Detailed Analysis
    # =====================================

    def analyze(self, text):


        prediction = self.predict(text)


        return {


            "text": text,


            "sentiment":
                prediction["label"],


            "confidence":
                prediction["confidence"],


            "model":
                self.model_name


        }




    # =====================================
    # Health Check
    # =====================================

    def status(self):

        return {


            "model":
                self.model_name,


            "available":
                self.classifier is not None

        }




# Global object used by Flask

sentiment_analyzer = SentimentAnalyzer()