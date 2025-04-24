from flask import Flask, jsonify, request
from createTableOperation import createTable
from addOperation import createUser, addProduct
from authUser import authenticate_user
from readOperations import getAllUsers, getSpacificUser
from updateOperation import update_approve_user, update_user_all_info
from deleteOperation import deleteUser

app = Flask(__name__)

@app.route("/createUser", methods = ["POST"])
def create_user():
    try:
        name = request.form["name"]
        password = request.form["password"]
        phoneNumber = request.form["phoneNumber"]
        email = request.form["email"]
        pinCode = request.form["pinCode"]
        address = request.form["address"]
        response = createUser(name = name, password = password, phoneNumber  = phoneNumber, email= email, pinCode= pinCode, address= address)
        return jsonify({'status' : 200, 'message': response})
    except Exception as error:
        return jsonify({"message" : error, "status" : 400})
    
@app.route("/login", methods = ["POST"])
def login_user():
    try:
        email = request.form["email"]
        password = request.form["password"]

        user = authenticate_user(email= email, password= password)
        if user:
            return jsonify({"status" : 200, "message": user[1]})
        else:
            return jsonify({"status" : 401, "message" : "Invalid email or password"})
        


    except Exception as error:
        return jsonify({"message" : error, "status" : 400})
    

#this is for get all the users and this will use in admin app
@app.route("/getAllUsers", methods =["GET"])
def get_All_Users():
    try:
        return jsonify(getAllUsers())

    except Exception as error:
        return jsonify({"message": error, "status": 400})

@app.route("/getSpacificUser", methods = ["POST"])
def get_Spacific_User():
    try:
        user_Id = request.form["userId"]
        user = getSpacificUser(userID = user_Id)
        return jsonify(user)
    except Exception as error:
        return jsonify({"message": "getting error", "status" : 400})

@app.route("/approveUser", methods= ["PATCH"])
def approve_User():
    try:
        user_Id = request.form["user_id"]
        approve = request.form["approve"]
        update_approve_user(userId=user_Id, approve=approve)
        return jsonify({"status": 200, "message": "Approval successfull"})
    except Exception as error:
        return jsonify({"message": error, "status" : 400})
    
@app.route("/updateAll", methods = ["PATCH"])
def update_all():
    try:
        user_id = request.form['user_id']
        upadteUser = {}

        for key, value in request.form.items():
            if key != "user_id":
                upadteUser[key] = value
        update_user_all_info(upadteUser, user_id)
        return jsonify({"status" : 200, 'message':'Update successful'})

    except Exception as error:
        return jsonify({"message": error, "status" : 400})
@app.route('/deleteUser', methods = ['DELETE'])
def delete_User():
    try:
        userId = request.form['userId']
        deleteUser(userId= userId)
        return jsonify({'status': 200, 'message': 'User deleted successfully'})
    except Exception as error:
        return jsonify({"message": error, "status" : 400})

    

@app.route('/addProduct', methods = ['POST'])
def add_Product():
    try:
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        stock = request.form['stock']
        addProduct(name= name, price= price, category= category, stock= stock)
        return jsonify({"status" : 200, 'message':'Product add successful'})
    except Exception as error:
        return jsonify({"message": error, "status" : 400})
if __name__=="__main__":
    createTable()
    app.run(debug=True)