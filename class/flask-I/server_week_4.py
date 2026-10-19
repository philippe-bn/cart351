from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("pineapples.html")

@app.route('/favfruit')
def pineapple():
    return render_template("pineapple_two.html")

@app.route('/three')
def three():
    someNewVar = "Sabine"
    return render_template("pineapple_three.html", my_variable = someNewVar)

@app.route('/four')
def four():
    a_new_list = [1,2,3,4,5]
    b_new_list = ["yellow","orange","blue", "green", "turquoise","fuscia","navy"]
    return render_template("pineapple_four.html", 
                           a_num_list = a_new_list,
                           color_list = b_new_list)

@app.route('/five')
def five():
    userLoggedIn = False
    return render_template("pineapple_five.html", 
                           user_bool = userLoggedIn)


app.run(debug=True)