import sqlite3

def deleteUser(userId):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Users WHERE user_id = ?", (userId,))
    conn.commit()
    conn.close()