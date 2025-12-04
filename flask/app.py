from flask import Flask 

### WSGI Applicattion 
app=Flask(__name__)  # Initializing the WSGI and passing parameter which is the entry point of this application 

'''
It creates an instance of the Flask class, 
which will be your WSGI (web server gateway interface) application 

'''

@app.route("/")
def welcome():
    return "Welcome to this flask application. This is the landing page of my flask application" 

@app.route("/index")
def index():
    return "Welcome to this flask application. This is the index page of my flask application" 

if __name__=="__main__":  # This is entry point for any .py file, this is the steps from where the execution starts 
    app.run(debug=True)  # Running the application in debug mode so that any changes made in the code will be reflected without restarting the server
