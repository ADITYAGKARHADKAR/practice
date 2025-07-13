from flask import Flask,request,jsonify,render_template
import json,os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/template_practice",methods=['GET'])

def templaterender():
    return render_template('c.html')



app.run(debug=True)