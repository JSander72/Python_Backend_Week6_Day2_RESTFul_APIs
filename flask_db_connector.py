from flask import Flask
from flask_marshmallow import Marshmallow
import mysql.connector

app = Flask(__name__)
ma = Marshmallow(app)

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12wsxdr56",
        database="flask_db"
    )
    return connection

# Test the connection
with get_db_connection() as conn:
    print("Database connected successfully!")

if __name__ == "__main__":
    app.run(debug=True)

