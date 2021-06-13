from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(filename = 'app.log', level=logging.DEBUG, format = f'%(asctime)s %(module)s : %(message)s')

@app.route("/")
def hello():
    app.logger.debug("/ endpoint was reached!")
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.debug("/status endpoint was reached!")
    healthz = {
        "result": "OK - healthy"
    }
    return healthz, 200

@app.route("/metrics")
def metrics():
    app.logger.debug("/metrics endpoint was reached!")
    metrics = {
        "UserCount": 140,
        "UserCountActive": 23
    }
    return metrics, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
