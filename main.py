import os
import json
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/journal')
def journal():
    return render_template("journal.html")

app.run(debug = True)