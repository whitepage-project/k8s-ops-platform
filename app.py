from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <h1>K8S Auto Recovery Platform</h1>
    <p>Service Status : Running</p>
    <p>Version : v1.0</p>
    <p>Hostname : {hostname}</p>
    <p>Current Time : {now}</p>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)