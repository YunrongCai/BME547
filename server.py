from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/",methods=["GET"])
def server_status():
    return "Server On"

@app.route("/info",methods=["GET"])
def info_route():
    return "This is true"

@app.route("/HDL_analysis",methods=["Post"])
def HDL_route_handler():
    in_data = request.get_json()
    from blood_calculator import HDL_analysis
    diagnosis = HDL_analysis(in_data['HDL_value'])
    return diagnosis

@app.route("/Add",methods=["Post"])
def Add_route_handler():
    in_data = request.get_json()
    answer = in_data["a"] + in_data["b"]
    print("The two numbers are : {} {}".format(in_data["a"],in_data["b"]))
    if answer < 0:
        return "The answer was less than zero. BAD", 400
    return jsonify(answer)

@app.route("/add_two/<a>/<b>", methods=["GET"])
def add_two_handler(a,b):
    answer = int(a) + int(b)
    return jsonify(answer)


if __name__ == '__main__':
    app.run()