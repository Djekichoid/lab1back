from flask import Flask, jsonify
from datetime import datetime
from myapp import app

@app.route("/")
def all_works():
    return f"<p>Hello world! Its my laboratory work 1</p><a href='/healthcheck'>Healthcheck</a>"


@app.route("/healthcheck")
def healthcheck():
    response = jsonify(date=datetime.now(), status="OK")
    response.status_code = 200
    return response
