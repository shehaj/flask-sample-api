from flask import Flask, jsonify
import psutil

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/index")
def index():
    return "<p>Index page!</p>"


@app.route("/processes")
def show_processes():
    processes = psutil.process_iter()
    processes_list = []
    for process in processes:
        processes_list.append({"Process ID": process.pid, "Name": process.name()})
    return jsonify(processes_list)
