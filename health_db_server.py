"""
Database = Dictionary
keys -> ids for the patients
value: dict

{
1:{"id":1, "name":"David", "bloodtype":"O+"},
2:{"id":2, "name":"David", "bloodtype":"O-"},
3:{"id":3, "name":"David", "bloodtype":"O+", "test":[]}
}
"""
from flask import Flask, request, jsonify

db = {}

app = Flask(__name__)

def add_patient_to_db(id, name, blood_type):
    new_patient ={"id": id,
                  "name": name,
                  "blood_type": blood_type,
                  "test": []
                  }
    db[id] = new_patient

def add_test_to_db(id, test_name, test_result):
    new_test ={"id": id,
               "test_name": test_name,
               "test_result": test_result}
    db[id]["test"].append(new_test)

@app.route("/add_test", methods=["POST"])
def post_add_test():
    in_data = request.get_json()
    answer, status_code = add_test_driver(in_data)
    return jsonify(answer)

@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    in_data = request.get_json()
    answer, status_code = new_patient_driver(in_data)
    return jsonify(answer)
def add_test_driver(in_data):
    validation = validate_input_data_test(in_data)
    if validation is not True:
        return validation, 400
    add_test_to_db(in_data["id"], in_data["test_name"], in_data["test_result"])
    return "Test successfully added", 200
def new_patient_driver(in_data):
    validation = validate_input_data(in_data)
    if validation is not True:
        return validation, 400
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    return "Patient successfully added", 200

def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["name", "id", "blood_type", "test"]
    expected_types = [str, int, str, list]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True

def validate_input_data_test(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


if __name__ == '__main__':
    app.run()