from flask import Flask, request, jsonify
import json, os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "employees.json")

@app.route('/search_employee', methods=['GET'])
def searchemployee():
    empno = request.args.get('empno')
    print("empno=",empno,type(empno))
    if empno is None or empno.strip()=="":
        return jsonify({"Error":"Bad request"}),400
    try:
        with open(FILE_PATH, "r") as f:
            allemployees = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return jsonify({"message": "No file found."}), 404

    for s in allemployees:
        if str(s['empno']) == str(empno):  
            print("I am inside if")
            return jsonify({
                "empno": s["empno"],  
                 "ename": s.get("ename", s.get("empname", "Unknown")),
                "salary": s["salary"]
            }), 200

    return jsonify({"Error": "Employee not found."}), 404  


@app.route('/get_employee',methods=['GET'])
def getemployee():
    ename=request.args.get('ename')
    if ename is None or ename.strip()=="":
        return jsonify({"Error":"Missing mandatory query parameter ename"}),400
    z=[]
    allemployees=[]
    try:
        with open("employees.json","r") as f:
            allemployees=json.load(f)
    except(FileNotFoundError,json.decoder.JSONDecodeError):
        return jsonify({"Error":"File does not exist"}),404
    
    for emp in allemployees:
        print("emp[ename]=",emp['ename'],"ename=",ename)
        if str(emp['ename'])==str(ename):
        
            print("I am inside if")
            z.append(emp)
    return jsonify(z),200

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        "Error": "Method Not Allowed",
        "message": f"Method {request.method} not allowed on {request.path}"
    }), 405

@app.route('/update_employee', methods=['PUT'])
def update_employee():

        data = request.get_json()
        ename=data.get('ename')
        sal=data.get('salary')
        if ename is None and sal is None:

            return jsonify({"Error":"At least one updatable parameter (ename or salary) should be provided"}),404
        empno = data.get('empno')

        if empno is None:
            return jsonify({"error": "empno is required"}), 400

        try:
            with open(FILE_PATH, "r") as f:
                employees = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return jsonify({"error": "Employee data file not found or invalid"}), 404

        updated = False
        for emp in employees:
            if emp["empno"] == data['empno']:
                if "ename" in data:
                    emp["ename"] = data["ename"]
                if "salary" in data:
                    emp["salary"] = data["salary"]
                updated = True
                break

        if not updated:
            return jsonify({"error": "Employee not found"}), 404

        
        with open(FILE_PATH, "w") as f:
            json.dump(employees, f, indent=2)

        return jsonify({"message": "Employee updated successfully!"}), 200


@app.route("/delete_employee",methods=['DELETE'])
def delete_employee():
    empno=request.args.get('empno')
    
    print("i am in delete method empno=",empno,"type(empno)=",type(empno))
    if empno is None or empno.strip()=="":
        return jsonify({'Error':"Bad Request"}),400
    updated=False
    all_employees=[]
    empno=int(empno)
    try:
        with open(FILE_PATH,"r") as f:
            all_employees=json.load(f)
    except FileNotFoundError:
        print("File not found",FILE_PATH)
    found=any(e['empno']==empno for e in all_employees)
    if found:
        all_employees=list(filter(lambda x:x['empno']!=empno,all_employees))
        print("all employees after deletion",all_employees)
    else:
        print("employee not found abcj")
        return jsonify({'error':"Employee not found abc"}),404
        
    # for i,emp in enumerate(all_employees):
    #     print("i am inside the loop","empno=",empno,"emp['empno']=",emp['empno'],type(emp['empno']))
    #     if emp['empno']==empno:
    #         updated=True
    #         del all_employees[i]
    # if updated==False:
    #     return jsonify({'error':"Employee not found"}),404
    try:
        with open(FILE_PATH,"w") as f:
            json.dump(all_employees,f,indent=2)
            return jsonify({"message":"employee deleted successfully"}),200
    except FileNotFoundError:
        print("File not found",FILE_PATH)

        











if __name__ == "__main__":
    app.run(debug=True)
