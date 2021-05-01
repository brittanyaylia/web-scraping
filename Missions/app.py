# flask
# creating route /scrape that will import scrape_mars.py 

import scrape_mars
import pymongo
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import sys

#flask app
app = Flask(__name__)

#mongo
mongo = PyMongo(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"

#index route to query mongodb & add data to html template
@app.route("/")
def index():

    print("mongo")
    mars_info = mongo.db.mars_db.find_one()

    print("html")
    return render_template("index.html", mars_data = mars_info)

#scrape route
@app.route("/scrape")
def scrape():

    mars_data = scrape_mars.news()
    mars_data = scrape_mars.featured_image()
    mars_data = scrape_mars.mars_facts()
    mars_data = scrape_mars.hemispheres()
    mongo.db.mars_db.update({}, mars_data, upsert=True)

    print("redirect")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)