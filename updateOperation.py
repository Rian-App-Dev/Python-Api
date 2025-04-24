import sqlite3

def update_approve_user(userId, approve):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Users SET isApproved = ? WHERE user_id = ?",(approve, userId))
    conn.commit()
    conn.close()

def update_user_all_info(updateList: dict, userId):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    for key, value in updateList.items():
        cursor.execute(f"UPDATE Users SET {key} = ? WHERE user_id = ?", (value, userId))
        # if key == "password":
        #     cursor.execute("UPDATE Users SET password = ? WHERE user_id = ?", (value, userId))
        # elif key == "isApproved":
        #     cursor.execute("UPDATE Users SET isApproved = ? WHERE user_id = ?", (value, userId))
        # elif key == "block":
        #     cursor.execute("UPDATE Users SET block = ? WHERE user_id = ?", (value, userId))
        # elif key == "name":
        #     cursor.execute("UPDATE Users SET name = ? WHERE user_id = ?", (value, userId))
        # elif key == "address":
        #     cursor.execute("UPDATE Users SET address = ? WHERE user_id = ?", (value, userId))
        # elif key == "email":
        #     cursor.execute("UPDATE Users SET email = ? WHERE user_id = ?", (value, userId))
        # elif key == "phone_number":
        #     cursor.execute("UPDATE Users SET phone_number = ? WHERE user_id = ?", (value, userId))
        # elif key == "pin_code":
        #     cursor.execute("UPDATE Users SET pin_code = ? WHERE user_id = ?", (value, userId))
        
    


    

    conn.commit()
    conn.close()