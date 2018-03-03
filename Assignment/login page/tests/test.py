from flask import Flask, redirect, render_template, request, url_for
from server import app

answer = "Hi"
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("please look at me")
        answer = request.form["gender"]
        print("%s" % answer)
        
        return redirect(url_for("result",answer=answer))
    return render_template("test.html")
    
@app.route("/result/<answer>")
def result(answer):

   return render_template("return.html",gender=answer)
   
   
   
   
   
   
