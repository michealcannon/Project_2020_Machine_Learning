# flask for web app.
import flask as fl
# Numerical arrays
import numpy as np
# Data frames.
import pandas as pd
# Plotting
import matplotlib.pyplot as plt
# neural neworks
import tensorflow.keras as kr
from flask import Flask, jsonify, request, abort, render_template, redirect, url_for, session, flash


# load model saved as .h5 file
#  code  from here https://machinelearningmastery.com/save-load-keras-deep-learning-models/#:~:text=Keras%20separates%20the%20concerns%20of,different%20formats%3A%20JSON%20and%20YAML.
model = kr.models.load_model('model.h5')

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add /power route.
@app.route('/power', methods=['POST', 'GET'])
def power():
  input = fl.request.args.get('input')  # input from web page assigned to variable input
  x = float(input)      # change input to float
  if x <=24:                    # only allow inputs less than/equal to 24 as model predicts lots of zero values after this
    value = model.predict([x])        # apply model to user input
    output = str(round(value[0][0], 3))     # have to extract the value from the matrix here and change to string to allow json return - round to 3 dp
    return {"html" : output}  # return as html... code adapted from https://stackoverflow.com/questions/50042492/call-flask-function-from-form-and-display-results-on-same-page
  else:
    return {"html": "Reliable outputs can not be provided for inputs greater than 24"}  # error message





