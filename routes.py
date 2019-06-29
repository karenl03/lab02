from flask import Flask, render_template #function is render template

app = Flask(__name__) #creating new usable instance of Flask class and saves to variable app

@app.route("/") #map URL "/" to python function index
def index(): #uses flask  to render index.html
	return render_template("index.html")
if __name__ == "__main__": #when user types url "/", function will run and return to page index.html
	app.run(debug=True) #will see any error messages

