"""
=========================================================
SentiVision AI
Database Management Module

Developed by:
Emad Ali
UID: 24BSC10027
=========================================================
"""

import sqlite3
from datetime import datetime
import logging


DATABASE_NAME = "sentiment_history.db"



class DatabaseManager:


    def __init__(self):

        self.database = DATABASE_NAME



    # ======================================
    # Initialize Database
    # ======================================

    def initialize(self):

        connection = sqlite3.connect(
            self.database
        )

        cursor = connection.cursor()


        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS history (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                text TEXT NOT NULL,

                sentiment TEXT NOT NULL,

                confidence REAL NOT NULL,

                created_at TEXT NOT NULL

            )
            """
        )


        connection.commit()

        connection.close()



    # ======================================
    # Save Analysis
    # ======================================

    def save_analysis(
            self,
            text,
            sentiment,
            confidence
    ):


        connection = sqlite3.connect(
            self.database
        )

        cursor = connection.cursor()


        cursor.execute(
            """
            INSERT INTO history

            (
                text,
                sentiment,
                confidence,
                created_at
            )

            VALUES (?,?,?,?)

            """,

            (

                text,

                sentiment,

                confidence,

                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

            )

        )


        connection.commit()

        connection.close()



    # ======================================
    # Get History
    # ======================================

    def get_history(self):


        connection = sqlite3.connect(
            self.database
        )


        connection.row_factory = sqlite3.Row


        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT *

            FROM history

            ORDER BY id DESC

            """
        )


        rows = cursor.fetchall()


        connection.close()


        return rows




    # ======================================
    # Statistics
    # ======================================

    def statistics(self):


        connection = sqlite3.connect(
            self.database
        )


        cursor = connection.cursor()



        cursor.execute(
            "SELECT COUNT(*) FROM history"
        )

        total = cursor.fetchone()[0]



        cursor.execute(
            """
            SELECT COUNT(*)

            FROM history

            WHERE sentiment='POSITIVE'

            """
        )

        positive = cursor.fetchone()[0]



        cursor.execute(
            """
            SELECT COUNT(*)

            FROM history

            WHERE sentiment='NEGATIVE'

            """
        )

        negative = cursor.fetchone()[0]



        cursor.execute(
            """
            SELECT COUNT(*)

            FROM history

            WHERE sentiment='NEUTRAL'

            """
        )

        neutral = cursor.fetchone()[0]



        cursor.execute(
            """
            SELECT AVG(confidence)

            FROM history

            """
        )


        average = cursor.fetchone()[0]


        connection.close()



        return {


            "total": total,


            "positive": positive,


            "negative": negative,


            "neutral": neutral,


            "average_confidence":
                round(average or 0,2)

        }





# Global database object

database = DatabaseManager()