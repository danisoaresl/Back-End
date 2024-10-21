from flask import Flask, render_template, request
import requests


SITE_KEY = "6Lc9ppUpAAAAAF6VD3pZKF1tE2NWoQ5rnr-G2yQx"
SECRET_KEY = "6Lc9ppUpAAAAAAMn1-N2drONVSzi06kW_IpYqDMc"

@app.route('/')
def index():
    return render_template('index.html', site_key=SITE_KEY)

@app.route("/submit", methods=["POST"])
def submit():
    recaptcha_response = requests.get("g-recaptcha-response")   
    
    if recaptcha_response:
        payload = {
            'secret': SECRET_KEY, 
            'response': recaptcha_response
        } 

if _name_ == '_main':
    app.run(debug=True, port=8085)