from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route("/pineappleParent")
def pineParent():
    return render_template("pineappleParent.html",)

@app.route("/pineappleA")
def pineAppleA():

    return render_template("pineappleChild.html",
                           dataPassedA = "child A!" )

@app.route("/pineappleB")
def pineAppleB():

    return render_template("pineappleChild_B.html",
                           passedImg = "../static/images/pineapple_2.jpg" )

@app.route("/")
def index():
    return render_template("index.html",
                           user={"username":"sabine"},
                           passedDictionary={
                                            "fav_color":"fuscia", 
                                             "fav_veg":"cauliflower",
                                             "fav_fruit":"kiwi",
                                             "fav_animal":"toucan"
                                             },
                            imgPath = "../static/images/pineapple_2.jpg"
                                        
                        )

@app.route("/inputPlant")
def addPlantData():
    return render_template("addPlantData.html") 

@app.route("/thank_you")
def thank_you():
    app.logger.info(request.args)
  
    if('o_name' in request.args):
        owner_name = request.args["o_name"] 
        app.logger.info("first run to redirect")
         #url is not clean
        #return render_template("thankyou.html",plantData = request.args) 
        
        # issue we lose the parameters! - but url is clean :)
        return redirect(url_for("thank_you")) 
    #part of the reloading process... we redirect - then headers rewritten and reload the template
    else:
        app.logger.info("reloaded and redirected")
        return render_template("thankyou.html") 

@app.route("/register")
def register():
     return render_template("register.html")

@app.route("/reg_thank_you",methods = ['POST', 'GET'])
def reg_thank_you():
     app.logger.info(request.form)
     app.logger.info(request.form["f_name"])
     app.logger.info(request.form["l_name"])
     return render_template("thankyou_reg.html", 
                            fName = request.form["f_name"],
                            lName = request.form["l_name"])

app.run(debug=True)