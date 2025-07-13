from flask import Flask,request,jsonify
import json,os
from flask_cors import CORS
app=Flask(__name__)
CORS(app)  
@app.route('/save_my_employee',methods=['POST'])

def saveemployee():
    data=request.json
    allemployees=[]
    try:
        with open("employees.json","r") as f:
            allemployees=json.load(f)
    except FileNotFoundError:
        print("I am in ecept")
        allemployees=[]
    print("I am before for",allemployees)
    for s in allemployees:
        print("s[empno]=",s["empno"],"data[empno]=",data["empno"])
        if s["empno"] == data["empno"]:
            return jsonify({"message": "Student Already exists!"}),409
    allemployees.append(data)


    with open('employees.json',"w") as f:
        json.dump(allemployees,f,indent=2)
        return jsonify({"message": "Employee Saved successfully!"}),201
    
@app.route('/save_my_student',methods=['POST'])


def savestudent():
    data=request.json
    allstudents=[]
    try:
        with open("students.json","r") as f:
            allstudents=json.load(f)
    except FileNotFoundError:
        allstudents=[]
    for s in allstudents:
        print("s[rollno]=",s["rollno"],"data[rollno]=",data["rollno"])
        if s["rollno"] == data["rollno"]:
            return jsonify({"message": "Student Already exists!"}),409
    allstudents.append(data)
    with open("students.json","w") as f:
        json.dump(allstudents,f,indent=2)
        return jsonify({"message":"Student is saved successfully"}),201














app.run(debug=True)