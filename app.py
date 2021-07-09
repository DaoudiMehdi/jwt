
from flask import Flask  ,request , jsonify,render_template
import requests
import json
import jwt
from datetime import datetime, timedelta



app=Flask(__name__)
app.config['SECRET_KEY']= 'Mehdi'

    
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login" , methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        token= jwt.encode({"name": request.form.get("name"), "exp": datetime.utcnow() +timedelta(minutes=5)},app.config["SECRET_KEY"])
        return jsonify({'message': 'succes','token':token}),200
    return jsonify({'message': 'failure'}) ,401

if __name__ == "__main__":
    app.run(debug=True)

