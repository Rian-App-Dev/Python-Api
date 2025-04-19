import sqlite3
from uuid import uuid4
from datetime import date
from flask import jsonify

def createUser(name, password, phoneNumber, email, pinCode, address):
    try:
        conn = sqlite3.connect("my_medicalShop.db")
        cursor = conn.cursor()

        userId = str(uuid4())
        dateOfAccountCreation = date.today()

        cursor.execute(
            '''INSERT INTO Users(user_id, password, date_of_account_creation, isApproved, block, name, address, email, phone_number, pin_code) VALUES(?,?,?,?,?,?,?,?,?,?)

    ''', (userId, password, dateOfAccountCreation, 0, 0, name, address, email, phoneNumber, pinCode)
    )

        conn.commit()
        conn.close()
        return jsonify({"message" : userId, "status" : 200})
    except Exception as error:
        return jsonify({"message" : error, "status" : 400})