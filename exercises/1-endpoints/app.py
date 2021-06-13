from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    healthz = {
        "result": "OK - healthy"
    }
    return healthz, 200

@app.route("/metrics")
def metrics():
    metrics = {
        "UserCount": 140,
        "UserCountActive": 23
    }
    return metrics, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
