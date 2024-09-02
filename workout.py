
from flask import Flask, request
from flask_marshmallow import Marshmallow
import mysql.connector

app = Flask(__name__)
ma = Marshmallow(app)

# schedule
@app.route('/workouts', methods=['POST'])
def schedule_workout():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "INSERT INTO WorkoutSessions (member_id, session_date, duration) VALUES (%s, %s, %s)"
    values = (data['member_id'], data['session_date'], data['duration'])
    cursor.execute(sql, values)
    connection.commit()

    return {"message": "Workout session scheduled successfully!"}, 201


# get workouts for a member
@app.route('/workouts/<int:member_id>', methods=['GET'])
def get_db_connection():
    # Implement your database connection logic here
    # Return the database connection object
    pass

@app.route('/workouts', methods=['POST'])
def schedule_workout():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "INSERT INTO WorkoutSessions (member_id, session_date, duration) VALUES (%s, %s, %s)"
    values = (data['member_id'], data['session_date'], data['duration'])
    cursor.execute(sql, values)
    connection.commit()

    return {"message": "Workout session scheduled successfully!"}, 201


# update workout session
@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "UPDATE WorkoutSessions SET session_date = %s, duration = %s WHERE id = %s"
    values = (data['session_date'], data['duration'], id)
    cursor.execute(sql, values)
    connection.commit()

    return {"message": "Workout session updated successfully!"}, 200


# delete workout session

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM WorkoutSessions WHERE id = %s", (id,))
    connection.commit()

    return {"message": "Workout session deleted successfully!"}, 200
