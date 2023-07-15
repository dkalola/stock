from flask import Flask
from flask import Flask, render_template
import requests
import yfinance as yf 


# Create an instance of the Flask application
app = Flask(__name__)

# Define a route and its corresponding handler function
@app.route('/')
def hello():
    return render_template('index.html')

def get_stock_data(TIKER):
    stock = yf.Ticker(TIKER)
    stock = stock.history(period="max")



# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)