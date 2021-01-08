# Project 2020 Machine Learning and Statistics
Project for Machine Learning and Statistics Course
Author: Micheál Cannon

This repository contains files for the project in "Machine Learning and Statistics" in 2020.

I created a web service that uses machine learning to make predictions based on the data set powerproduction.
I then developed a web service that responds with predicted power values based on speed values sent as HTTP requests. 
It contains:
1. A Jupyter notebook that trains a model using the data set, explains the model and gives an analysis of its accuracy.
2. A Python script that runs a web service based on the model.
3. A Dockerfile to build and run the web service in a container.
4. Standard files e.g. README, .gitignore, .dockerignore.

To Run in Windows:  
set FLASK_APP=web_app.py  
python -m flask run  

To Run in Linux:  
exort FLASK_APP = web_app.py  
python3 -m flask run  

Docker:
docker build . -t power-image  
docker run --name power-container -d -p 5000:5000 power-image
