"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa6vak728r8862buhg-a.oregon-postgres.render.com",
        database="todo_6h21",
        user="todo_6h21_user",
        password="JuWg4jH67eHttn3RFYqCGZI2hun5qSF4")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
