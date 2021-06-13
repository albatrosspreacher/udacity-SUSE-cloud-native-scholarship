from flask import Flask  #import the flask library

app = Flask(
    __name__)  #creates a flask instance with the name of the current module


@app.route("/")  #adds a route / to the flask application
def hello():  #defines a function that is called when the app route is /
    return "Hello World!"  #returns this value


@app.route("/status")  #adds a route /status to the flask application
def status():  #defines a function that is called when the app route is /status
    healthz = {"result": "OK - healthy"}
    return healthz, 200  #returns the variable along with status code 200


@app.route("/metrics")  #adds a route /metrics to the flask application
def metrics(
):  #defines a function that is called when the app route is /metrics
    metrics = {"UserCount": 140, "UserCountActive": 23}
    return metrics, 200  #returns the variable along with status code 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
