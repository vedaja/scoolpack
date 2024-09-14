from flask import Flask,render_template,request,redirect
import random
import sqlite3

app=Flask("veda")
app.debug=True

app.secret_key = "bheem"

@app.route("/", methods=["POST","GET"])
def homepage():
    if request.method=="GET":
        return render_template("homepage.html")

@app.route("/study", methods=["POST","GET"])
def study():
    if request.method=="GET":
        num1 = random.randrange(1, 10)
        num2 = random.randrange(1, 10)
        tog = num1 + num2
        return render_template('study.html', num1=num1, num2=num2, tog=tog)


@app.route("/organize", methods=["POST","GET"])
def organize():
    if request.method=="GET":
        return render_template("organize.html")

@app.route("/help", methods=["POST","GET"])
def help():
    if request.method=="GET":
        return render_template("help.html")

@app.route("/find",methods=["POST","GET"])
def find():
    if request.method=="GET":
        return render_template("find.html")

app.run()