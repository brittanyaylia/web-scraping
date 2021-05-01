# flask
# creating route /scrape that will import scrape_mars.py 

import scrape_mars
import pymongo
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import sys

#flask app
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_info"
mongo = PyMongo(app)

#index route to query mongodb & add data to html template
@app.route("/")
def index():

    mars = mongo.db.collection.find_one()
    return render_template("index.html", mars_info = mars)

#scrape route
@app.route("/scrape")
def scrape():

    mars = mongo.db.collection

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)