from flask import Flask
from flask import Flask, render_template


# Create an instance of the Flask application
app = Flask(__name__)

# Define a route and its corresponding handler function
@app.route('/')
def hello():
    return render_template('index.html')

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)