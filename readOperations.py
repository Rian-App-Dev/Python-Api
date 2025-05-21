import sqlite3

def getAllUsers():
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users")

    users = cursor.fetchall()
    userlist = []
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
        userlist.append(tempUser)
    conn.close()
    return userlist

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