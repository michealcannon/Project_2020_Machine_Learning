# flask for web app.
import flask as fl
# numerical work.
import numpy as np

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# TO RUN IN WINDOWS:
# set FLASK_APP=rando.py
# python -m flask run




