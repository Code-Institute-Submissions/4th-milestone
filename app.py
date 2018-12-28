import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'onlinecookbook'
app.config["MONGO_URI"] = 'mongodb://admin:Bettyboop234@ds139614.mlab.com:39614/onlinecookbook'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipe')
def get_recipe():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())
    
@app.route('/add_task')
def add_task():
    return render_template('addtasks.html')
    



# @app.route('/')
# def hello():
#     return "Hello World ...again"
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
