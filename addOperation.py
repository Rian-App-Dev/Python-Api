import sqlite3
from uuid import uuid4
from datetime import date
from flask import jsonify

def createUser(name, password, phoneNumber, email, pinCode, address):
    
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
    return userId
    
def addProduct(name, price, category, stock):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    productId = str(uuid4())
    cursor.execute(
        '''
INSERT INTO Products(product_id, name, price, category, stock) VALUES(?,?,?,?,?)
''', (productId, name, price, category, stock)
    )
    conn.commit()
    conn.close()
def orderDetails():
    conn = sqlite3.connect("my_medicalShop")
    cursor = conn.cursor()

    cursor.execute(
        '''
INSERT INTO Order_Details(order_id, user_id, product_id, isApproved, quantity, date_of_order_creation, price, total_amount, product_name, user_name, message, category) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
''', 
    )