from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return ' Hello CART 351!'

@app.route("/about")
def about():
    return '<h1 style = "color:purple"> About Cart 351!</h1>'

@app.route("/user/<name>")
def user_profile(name):
    # we will use templates sooN!
    return f"<h2> This is <span style = 'color:orange'>{name}'s</span> profile page"

# # if cat name[-1] is y, remove y add iful
# # if not append y
# @app.route("/catlatin/<name>")
# def cat_latin(name):
#     if (name[-1].lower() == "y"):
#         return f"{name[:-1]}iful"
#     return f"{name}y"

app.run()