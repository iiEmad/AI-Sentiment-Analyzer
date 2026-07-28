"""
=========================================================
SentiVision AI
Main Flask Application

Developed by:
Emad Ali
UID: 24BSC10027
=========================================================
"""

from flask import Flask, render_template, request
import logging

from database import database
from ai.sentiment import sentiment_analyzer
from ai.keywords import keyword_extractor
from ai.explanation import explanation_generator


# ==========================
# Flask Setup
# ==========================

app = Flask(__name__)


# ==========================
# Logging
# ==========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)



# ==========================
# Initialize Database
# ==========================

database.initialize()

logging.info(
    "Database initialized successfully."
)



# ==========================
# Home Page
# ==========================

@app.route("/", methods=["GET", "POST"])
def home():

    result = None


    if request.method == "POST":


        text = request.form.get(
            "text",
            ""
        ).strip()



        if text:


            # AI Prediction

            prediction = sentiment_analyzer.predict(
                text
            )


            sentiment = prediction["label"]

            confidence = prediction["confidence"]



            # Keywords

            keywords = keyword_extractor.extract(
                text
            )



            # Explanation

            explanation = explanation_generator.generate(

                sentiment,

                confidence,

                keywords

            )



            result = {

                "text": text,

                "sentiment": sentiment,

                "confidence": confidence,

                "keywords": keywords,

                "full_explanation":
                    explanation["full_explanation"]

            }



            # Save

            database.save_analysis(

                text,

                sentiment,

                confidence

            )



    return render_template(

        "index.html",

        result=result

    )




# ==========================
# History
# ==========================

@app.route("/history")
def history():


    records = database.get_history()


    return render_template(

        "history.html",

        history=records

    )




# ==========================
# Dashboard
# ==========================

@app.route("/dashboard")
def dashboard():


    stats = database.statistics()


    return render_template(

        "dashboard.html",

        stats=stats

    )




# ==========================
# About
# ==========================

@app.route("/about")
def about():


    return render_template(

        "about.html",

        developer="Emad Ali",

        uid="24BSC10027",

        version="3.0"

    )




# ==========================
# Error Handling
# ==========================

@app.errorhandler(404)
def page_not_found(error):


    return render_template(

        "error.html",

        error_code=404,

        message="Page not found"

    ),404




@app.errorhandler(500)
def server_error(error):


    return render_template(

        "error.html",

        error_code=500,

        message="Internal server error"

    ),500




# ==========================
# Run
# ==========================

if __name__ == "__main__":


    app.run(

        debug=True,

        host="127.0.0.1",

        port=5000

    )