from flask import Flask, render_template 
import joblib as joblib
import numpy as np


app = Flask(__name__) 

@app.route("/") 


def index(): 
	prediction = model.predict([[4, 2.5, 3005, 15, 17903.0]]).round(1)
	prediction = np.squeeze(prediction.tolist())
	prediction = str(prediction)
	return render_template("index.html", prediction=prediction)
if __name__ == '__main__':
    model = joblib.load('reg.pkl')
    app.run(debug=True)

