import sqlite3

def update_approve_user(userId, approve):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Users SET isApproved = ? WHERE user_id = ?",(approve, userId))
    conn.commit()
    conn.close()

def update_user_all_info():
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Users SET")

    conn.commit()
    conn.close()