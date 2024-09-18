# Imports
from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

# My App
app = Flask(__name__)


# Route for the home page
@app.route("/")
def index():
    return "Testing 123"


if __name__ == "__main__":
    app.run(debug=True)
