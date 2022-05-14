from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [
    {"contact": "9987644456", "name": "Raju", "done": False, "id": 1},
    {"contact": "9876543222", "name": "Rahul", "done": False, "id": 2},
]


@app.route("/add-data", methods=["POST"])
def addData():
    if not request.json:
        return jsonify({"status": "error", "message": "Please provide data"}, 400)

    newContact = {
        "id": contacts[-1]["id"] + 1,
        "contact": request.json["contact"],
        "name": request.json.get("name", ""),
        "done": False,
    }
    contacts.append(newContact)
    print(contacts)
    return jsonify({"status": "success", "message": "contact added Successfully!!!"})


@app.route("/get-data", methods=["GET"])
def getData():
    return jsonify({"contacts": contacts})


if __name__ == "__main__":
    app.run(debug=False)
