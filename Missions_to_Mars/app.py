from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import os


app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.mars_news
collection = db.articles


@app.route("/")
def home(): 

    mars_news = mongo.db.mars_news.find_one()

    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scrape(): 

    mars_news = mongo.db.mars_news
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.featured_image()
    mars_data = scrape_mars.mars_facts()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/")

if __name__ == "__main__": 
    app.run(debug= True)