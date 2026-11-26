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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port="port")

# - Can I run my other pages (like Exercise 2 and 3) directly through the same render?
# - Should I?
# - The POST method (353)
# - Running miniproject (same render or different, and cloudflare)