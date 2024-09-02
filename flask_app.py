
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_db_connector import get_db_connection
from flask import Flask, request
app = Flask(__name__)
ma = Marshmallow(app)

class MemberSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'join_date')

member_schema = MemberSchema()
members_schema = MemberSchema(many=True)


# add members 
@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "INSERT INTO Members (name, age, membership_date) VALUES (%s, %s, %s)"
    values = (data['name'], data['age'], data['membership_date'])
    cursor.execute(sql, values)
    connection.commit()

    return {"message": "Member added successfully!"}, 201

# get membwers

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
    member = cursor.fetchone()

    if member:
        return member, 200
    else:
        return {"error": "Member not found"}, 404


# update member

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "UPDATE Members SET name = %s, age = %s, membership_date = %s WHERE id = %s"
    values = (data['name'], data['age'], data['membership_date'], id)
    cursor.execute(sql, values)
    connection.commit()

    return {"message": "Member updated successfully!"}, 200


# delete member

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Members WHERE id = %s", (id,))
    connection.commit()

    return {"message": "Member deleted successfully!"}, 200

