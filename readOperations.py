import sqlite3

def getAllUsers():
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users")

    users = cursor.fetchall()
    userJson = []

# id INTEGER PRIMARY KEY AUTOINCREMENT,
# user_id VARCHAR(255),
# password VARCHAR(50),
# date_of_account_creation DATE,
# isApproved BOOLEAN,
# block BOOLEAN,
# name VARCHAR(255),
# address VARCHAR(255),
# email VARCHAR(255),
# phone_number VARCHAR(255),
# pin_code VARCHAR(255)

    for user in users:
        tempUser = {
            "id": user[0],
            "user_id": user[1],
            "password": user[2],
            "date_of_account_creation": user[3],
            "isApproved": user[4],
            "block": user[5],
            "name": user[6],
            "address": user[7],
            "email": user[8],
            "phone_number": user[9],
            "pin_code": user[10]
        }
        userJson.append(tempUser)
    conn.close()
    return userJson

def getSpacificUser(userID):
    conn = sqlite3.connect("my_medicalShop.db")
    cusrsor = conn.cursor()

    cusrsor.execute("SELECT * FROM Users WHERE user_id = ?",(userID,))
    user = cusrsor.fetchone()
    conn.close()
    tempUser = {
            "id": user[0],
            "user_id": user[1],
            "password": user[2],
            "date_of_account_creation": user[3],
            "isApproved": user[4],
            "block": user[5],
            "name": user[6],
            "address": user[7],
            "email": user[8],
            "phone_number": user[9],
            "pin_code": user[10]
        }
    return tempUser