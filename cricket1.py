from flask import Flask, request, jsonify
import json, os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "cricket.json")

@app.route('/save_my_cricketer', methods=['POST'])
def savecricketer():
    data = request.json
    try:
        with open(FILE_PATH, "r") as f:
            allcricketers = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        allcricketers = []

    for s in allcricketers:
        print("s[cno]=", s["cno"], "data[cno]=", data["cno"])
        if s["cno"] == data["cno"]:
            return jsonify({"message": "Cricketer Already exists!"}), 409

    allcricketers.append(data)

    with open(FILE_PATH, "w") as f:
        json.dump(allcricketers, f, indent=2)

    return jsonify({"message": "Cricketer Saved successfully!"}), 201

@app.route('/search_cricketer', methods=['GET'])
def searchcricketer():
    cno = request.args.get('cno')
    try:
        with open(FILE_PATH, "r") as f:
            allcricketers = json.load(f)
        print("allcricketers=", allcricketers)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return jsonify({"message": "No file found."}), 404

    for s in allcricketers:
        if str(s['cno']) == str(cno):
            print("I am inside if")
            return jsonify({
                "cno": s["cno"],
                "cname": s["cname"],
                "r": s["r"]
            }), 200

    return jsonify({"message": "Cricketer not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
