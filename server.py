from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET"])
def server_status():
    return "Server On"

@app.route("/info",methods=["GET"])
def info_route():
    return "This is true"


if __name__ == '__main__':
    app.run()