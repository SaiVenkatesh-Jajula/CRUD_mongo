from flask import Flask,request,jsonify
from flask_pymongo import pymongo
from bson.json_util import dumps
#CONNECTION FROM ATLAS TO LOCAL SYSTEM....
link= "mongodb+srv://venkatesh:venkatesh@cluster0.sfuytgu.mongodb.net/?retryWrites=true&w=majority"
client= pymongo.MongoClient(link)
database=client.get_database('database')
userCollection=pymongo.collection.Collection(database,'teachers')
print("Mongo Database Connected Sucessfully")

app=Flask(__name__)#WSGI


@app.route("/hello")
def hello():
    return "HelloWorld"

@app.route("/createUser",methods=['POST'])
def createUser():
    res={}
    try:
        req=request.json
        userCollection.insert_one(req)
        print("Insertion Sucess")
        r={"status":"Sucess"}
    except Exception as e:
        print(e)
        r={"status":"Failed"}
    res["response"]=r
    return res

@app.route("/readUsers",methods=['GET'])
def readUsers():
    result= userCollection.find()
    response=dumps(result)
    return response
    

@app.route("/updateUser",methods=['PUT'])
def updateUser():
    res={}
    try:
        req=request.json
        userCollection.update_one({"id":req['id']},{"$set":req['updated']})
        print("Updated Sucessfully")
        r={"status":"Sucess"}
    except Exception as e:
        print(e)
        r={"status":"Failed"}
    res["response"]=r
    return res

@app.route("/deleteUser",methods=['DELETE'])
def deleteUser():
    res={}
    try:
        id=request.args.get('deleteId')
        userCollection.delete_one({"id":id})
        print("Deleted Sucessfully")
        r={"status":"Sucess"}
    except Exception as e:
        print(e)
        r={"status":"Failed"}
    res["response"]=r
    return res       

if __name__=="__main__":
    app.run(debug=True)

"""
bcrypt converts password to hash    """