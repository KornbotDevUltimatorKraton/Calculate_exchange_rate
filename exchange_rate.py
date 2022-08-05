import requests
from flask import Flask,render_template,redirect,url_for,jsonify
token = "0391a7e6b5cdf4800aa6da57"
url = 'https://v6.exchangerate-api.com/v6/'+token+'/latest/USD'
app = Flask(__name__) 

@app.route('/')
def index():
     response = requests.get(url) 
     data = response.json() 
     return jsonify(data.get('conversion_rates')) #Getting the data of currency conversion rates 

if __name__ == "__main__":
       app.run(debug=True,threaded=True,host="0.0.0.0",port=8020) # Getting the port and ip number 
