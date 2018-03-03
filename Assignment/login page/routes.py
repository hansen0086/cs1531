from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input
import csv
from csv_fun import *

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        
        user_input.append([name, password])
        
        
        if(name=="hansen" and password=="123"):
        	return redirect(url_for("hello"))
        else:
        	return redirect(url_for("try_again"))
    return render_template("index.html")




@app.route("/Hello")
def hello():
    
    return render_template("hello.html") 
    
 
@app.route("/Try_again", methods=["GET", "POST"])
def try_again():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        
        user_input.append([name, password])
        
        
        if(name=="hansen" and password=="123"):
        	return redirect(url_for("hello"))
        else:
        	return redirect(url_for("try_again"))
    return render_template("try_again.html")
    
    
@app.route("/All_courses",methods=["GET","POST"])
def all_courses():
   courses = print_from_csv("all_courses.csv")
   return render_template("all_courses.html",courses=courses)

@app.route("/All_surveys",methods=["GET","POST"])
def all_surveys():
   return render_template("all_surveys.html")

@app.route("/All_questions",methods=["GET","POST"])
def all_questions():
   return render_template("all_questions.html")
   
   
@app.route("/Add_course",methods=["GET","POST"])
def add_courses():
   if request.method =="GET":
      return render_template("add_course.html")
   else:
      course_name = request.form["course_name"]
      write_to_csv("all_courses.csv",[course_name])
      creat_a_csv(course_name)
      return redirect(url_for("all_courses"))

@app.route("/Add_survey",methods=["GET","POST"])
def add_surveys():
   return render_template("add_survey.html")

@app.route("/Add_question",methods=["GET","POST"])
def add_questions():
   return render_template("add_question.html")
   
   
   
   
   
   
   

