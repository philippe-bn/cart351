from dotenv import load_dotenv
import os
from flask import Flask,render_template,request,redirect, url_for,session 
# use flask_pymongo instead of  normal pymongo (simplifies integration)
from flask_pymongo import PyMongo

load_dotenv()  # Load variables from .env and .flaskenv
db_user = os.getenv('MONGODB_USERNAME')
db_pass = os.getenv('MONGODB_PASSWORD')
print(db_user)
uri = os.getenv("MONGODB_URI")
db_name = os.getenv('DATABASE_NAME') 
uri = uri+f"/{db_name}?retryWrites=true&w=majority"

app = Flask(__name__)

# set a config var
app.config["MONGO_URI"] = uri
app.secret_key = 'BAD_SECRET_KEY'
mongo = PyMongo(app)
try:
    #get details of the client
    print (mongo.cx)
    #get db
    print (mongo.db)
    #get collection
    print (mongo.db.plantRepo)
    print("You successfully connected to MongoDB!")
    # result = mongo.db.plantRepo.insert_one({"testKeyMon":"testValueMon"})
    # print(result)
except Exception as e:
    print(e)


@app.route('/')
def index():
    return render_template("index.html")
app.run(debug = True)