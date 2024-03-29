# health_db_server.py
import logging
from flask import Flask, request, jsonify
from pymodm import connect
from PatientModel import Patient
from pymodm import errors as pymodom_errors

"""
Database Description: A dictionary of dictionaries.
keys -> ids for the patients
values -> Dictionary with patient information

Patient dictionary will look like this example:
  {"id": 1, "name": "David", "blood_type": "O+", "tests": []}

The "tests" list will be a series of tuples that contain the test
name and test result
"""

# Create a global variable to hold the database

# Create an instance of the Flask server
app = Flask(__name__)

def init_server():
    logging.basicConfig(filename="server.log", filemode="w")
    connect("mongodb+srv://yc551:<19961126ERIC>@bme547.fqdewfv.mongodb.net/BME547?retryWrites=true&w=majority")


def add_patient_to_db(patient_id, patient_name, blood_type):
    """ Adds a new patient dictionary to the database

    This function receives basic information on a new patient, creates a
    dictionary containing that information, as well as an empty list to hold
    test data to be added in the future, and adds this patient dictionary to
    the database dictionary using the patient id as a key.

    The database is being stored in an internal global variable.  As this
    variable is a dictionary that has already been created, and a dictionary
    is a mutable data type, the use of the "global" keyword is not required.

    The function also prints the database to the console so that we can see
    how the database is changing as the server is being used.

    Args:
        patient_id (int): The medical record number of the patient
        patient_name (str): Full name of patient
        blood_type (str): Blood type of the patient

    Returns:
        None
    """

    new_patient = Patient(patient_id=patient_id,
                          patient_name=patient_name,
                          blood_type =blood_type)
    saved_patient = new_patient.save()
    return saved_patient


def add_test_to_db(patient_id, test_name, test_value):
    """Adds test result for a specific patient.

    This function adds a test result to the specified patient.  The patient
    is found in the database using the patient_id as the key.  The "tests"
    key of the patient database is then used to access the tests list to
    which a tuple of the test_name and test_value is appended.  The database
    is then printed.

    Args:
        patient_id (int): The medical record number of the patient
        test_name (str): Name of the test to be added
        test_value (int): result of the test

    Returns:
        None
    """
    x = Patient.objects.raw({"_id": patient_id}).first()
    x.test.append((test_name,test_value))
    x.save()


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    """POST route to receive information about a new patient and add the
       patient to the database

    This "Flask handler" function receives a POST request to add a new patient
    to the database.  The POST request should receive a dictionary encoded as
    a JSON string in the following format:

        {"id": int,
         "name": str,
         "blood_type": str}

    The value of "id" is an integer that is the medical record number for the
    patient.  The value for "name" is a string that should contain the full
    name of the patient.  The value of "blood_type" is a string that
    contains the blood type of the patient (O+, O-, A+, A-, B+, B-, AB+, AB-).

    The function first receives the dictionary sent with the POST request.  It
    then calls a worker function to act on the data.  It finally returns the
    resulting message and status code.
    """
    # Receive data from POST request
    in_data = request.get_json()
    # Call other functions to do the work
    answer, status_code = new_patient_driver(in_data)
    # Return a response
    return jsonify(answer), status_code


def new_patient_driver(in_data):
    """Implements the '/new_patient' route

    This function performs the data validation and implementation for the
    `/new_patient` route which adds a new patient to the database.  It first
    calls a function that validates that the input data to the route is a
    dictionary that has the necessary keys and value data types.  If the
    necessary information does not exist, the function returns an error message
    and a status code of 400.  Otherwise, another function is called and sent
    the necessary information to add a new patient to the database.  A success
    message and a 200 status code is then returned.

    Args:
        in_data (dict): Data received from the POST request.  Should be a
        dictionary with the format found in the docstring of the
        "post_new_patient" function, but that needs to be verified

    Returns:
        str, int: a message with information about the success or failure of
            the operation and a status code

        """
    # Validate input
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    validation = validate_input_data_generic(in_data, expected_keys,
                                             expected_types)
    if validation is not True:
        return validation, 400
    # Do the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # Return an answer
    return "Patient successfully added", 200


def validate_input_data_generic(in_data, expected_keys, expected_types):
    """Validates that input data is a dictionary with correct information

    This function receives the data that was sent with a POST request.  It
    also receives lists of the keys and value data types that are expected to
    be in this dictionary.  The function first verifies that the data sent to
    the post request is a dictionary.  Then, it verifies that the expected keys
    are found in the dictionary and that the corresponding value data types
    are of the correct type.  An error message is returned if the data is not
    a dictionary, a key is missing or there is an invalid data type.  If keys
    and data types are correct, a value of True is returned.

    Args:
        in_data (dict): object received by the POST request
        expected_keys (list): keys that should be found in the POST request
            dictionary
        expected_types (list): the value data types that should be found in the
            POST request dictionary

    Returns:
        str: error message if there is a problem with the input data, or
        bool: True if input data is valid.

    """
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


@app.route("/add_test", methods=["POST"])
def post_add_test():
    """POST route to receive information about a test to add to a patient
    record in the database.

    This "Flask handler" function receives a POST request to add a test result
    to a patient record in the database.  The POST request should receive a
    dictionary encoded as a JSON string in the following format:

        {"id": int,
         "test_name": str,
         "test_result": int}

    The value of "id" is an integer that is the medical record number for the
    patient.  The value of "test_name" is a string containing the name of the
    test.  The value of "test_result" is an integer containing the numeric
    result of the test.

    The function first receives the dictionary sent with the POST request.  It
    then calls a driver function to act on the data.  It finally returns the
    resulting message and status code.
    """

    in_data = request.get_json()
    answer, status_code = add_test_driver(in_data)
    return jsonify(answer), status_code


def does_patient_exist_in_db(patient_id):
    """Determines whether a patient exists in the database based on a given id
    number

    This function accepts a patient id (medical record number) as an input
    parameter.  It then checks to see if this id is a key in the database
    dictionary.  If so, it returns True, otherwise returns False.

    Args:
        patient_id (int): patient medical record number to search for in the
            database

    Returns:
        bool: True if patient exists in database, False otherwise

    """
    try:
        db_item = Patient.objects.raw({"_id": patient_id}).first()
    except pymdom_errors.DoesNotExist




def add_test_driver(in_data):
    """Implements the '/add_test' route

    This function performs the data validation and implementation for the
    `/add_test` route which adds a new test result to the database entry
    for a specific patient.  It first calls a function that validates that
    the necessary keys and value data types exist in the input dictionary.
    If the necessary information does not exist, the function returns an
    error message and a status code of 400.  Next, another function is called
    to verify the specified patient exists in the database.  If not, an error
    message and a status code of 400 is returned.  Otherwise, another function
    is called and sent the necessary information to add the test results to
    the correct patient.  A success message and a 200 status code is then
    returned.

    Args:
        in_data (dict): Data received from the POST request.  Should be a
        dictionary with the format found in the docstring of the
        "post_add_test" function, but that needs to be verified

    Returns:
        str, int: a message with information about the success or failure of
            the operation and a status code
        """

    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    validation = validate_input_data_generic(in_data, expected_keys,
                                             expected_types)
    if validation is not True:
        return validation, 400
    does_id_exist = does_patient_exist_in_db(in_data["id"])
    if does_id_exist is False:
        return "Patient id {} does not exist in database"\
            .format(in_data["id"]), 400
    add_test_to_db(in_data["id"], in_data["test_name"],
                   in_data["test_result"])
    return "Test successfully added", 200

@app.route("/get_results/<patient_id>")
def get_get_results(patient_id):
    answer, status = get_result_driver(patient_id)
    return jsonify(answer), status

def get_result_driver(patient_id):
    validation = validate_patient_id_from_get(patient_id)
    if validation is not True:
        return validation, 400
    patient = db[int(patient_id)]
    return patient["tests"], 200

def validate_patient_id_from_get(patient_id):
    try:
        patient_num = int(patient_id)
    except ValueError:
        return "Patient_id should be an integer"
    if does_patient_exist_in_db(patient_num) is False:
        return "Patient_id of {} does not exist in database".format(patient_num)
    return True





if __name__ == '__main__':
    app.run()