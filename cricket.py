from flask import Flask,request,jsonify
import json,os
from flask_cors import CORS
import traceback 
app=Flask(__name__)
CORS(app)
@app.route('/save_my_cricketer',methods=['POST'])

def savecricketer():
    data=request.json
    allcricketers=[]
    try:
        with open("cricket.json","r") as f:
            allcricketers=json.load(f)
    except FileNotFoundError:
        allcricketers=[]
    for s in allcricketers:
        print("s[cno]=",s["cno"],"data[cno]=",data["cno"])
        if s["cno"] == data["cno"]:
            return jsonify({"message": "Cricketer Already exists!"}),409
    allcricketers.append(data)


    with open('cricket.json',"w") as f:
        json.dump(allcricketers,f,indent=2)
        return jsonify({"message": "Cricketer Saved successfully!"}),201

app.run(debug=True)