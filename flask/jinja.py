## Building Url Dynamically 
## Variable Rules
## Jinja 2 Template Engine 


## Jinja 2 Template Engine

'''
{{ variable }}  --> to print variable value
{% for item in list %}  --> for loop
{%...%}  --> for conditional statements
{#...#}  --> for comments
'''

from flask import Flask, render_template, request, redirect, url_for


# render_template is used to render HTML files, to redirect to HTML pages
### WSGI Applicattion 
app=Flask(__name__)  # Initializing the WSGI and passing parameter which is the entry point of this application 

'''
It creates an instance of the Flask class, 
which will be your WSGI (web server gateway interface) application 

'''

@app.route("/")
def welcome():
    return "<html><H1>Welcome to this flask application. This is the landing page of my flask application</H1></html>" 

@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/submit",methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name = request.form['name']
#         email = request.form['email']
#         return f"<html><H1>Form submitted successfully! Name: {name}, Email: {email}</H1></html>"
#     return render_template("submit.html")


## Variable Rules

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    return render_template("result.html",result=res)


@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score>=50:
        res="passed the exam"
    else:
        res="failed the exam"

    exp = {'score':score,'result':res}
    return render_template("result1.html",result=exp)

## If condition 

@app.route("/successif/<int:score>")
def successif(score):
    
    return render_template("result.html",result=score)


@app.route("/fail/<int:score>")
def fail(score):
   
    return render_template("result.html",result=score)

@app.route("/submit",methods=['GET','POST'])
def submit():
    total_score=0
    if request.method=='POST':
        math = float(request.form['math'])
        science = float(request.form['science'])
        english = float(request.form['english'])
        total_score = (math + science + english)/3
    else:
        return render_template("getresult.html")
    return redirect(url_for('successres',score=total_score))  

if __name__=="__main__":  # This is entry point for any .py file, this is the steps from where the execution starts 
    app.run(debug=True)  # Running the application in debug mode so that any changes made in the code will be reflected without restarting the server
