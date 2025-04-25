from flask import Flask, jsonify, request
from createTableOperation import createTable
from addOperation import createUser
from authUser import authenticate_user
from readOperations import getAllUsers, getSpacificUser
from updateOperation import update_approve_user, update_user_all_info

app = Flask(__name__)

@app.route('/data', methods = ['GET'])
def hello():
    return jsonify({"Name" : "Rian", "Age" : 21, "Phone" : 8801756111949})

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
        return response
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



if __name__=="__main__":
    createTable()
    app.run(debug=True)