import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'onlinecookbook'
app.config["MONGO_URI"] = 'mongodb://admin:Bettyboop234@ds149914.mlab.com:49914/poembook'


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_poems')
def get_poems():
    return render_template("poems.html", 
    poems=mongo.db.poems.find())
    
    
@app.route('/add_poem')
def add_poem():
    return render_template('addpoems.html',
    genres=mongo.db.genres.find())

@app.route('/view_poem')
def view_poem():
    return render_template('viewpoems.html',
    poems=mongo.db.poems.find())
    
@app.route('/insert_poem', methods=['POST'])
def insert_poem():
    poems =  mongo.db.poems
    poems.insert_one(request.form.to_dict())
    return redirect(url_for('get_poems'))
    
@app.route('/edit_poem/<poem_id>')
def edit_poem(poem_id):
    the_poem =  mongo.db.poems.find_one({"_id": ObjectId(poem_id)})
    all_genres =  mongo.db.genres.find()
    return render_template('editpoem.html', poems=the_poem, genres=all_genres)
    
@app.route('/update_poem/<poem_id>', methods=["POST"])
def update_poem(poem_id):
    poems = mongo.db.poems
    poems.update( {'_id': ObjectId(poem_id)},
    {
        'poem_name':request.form.get['poem_name'],
        'genre_name':request.form.get['genre_name'],
        'poem_description': request.form.get['poem_description'],
       
    })
    return redirect(url_for('get_poems'))
    
@app.route('/delete_poem/<poem_id>')
def delete_poem(poem_id):
    mongo.db.poems.remove({'_id': ObjectId(poem_id)})
    return redirect(url_for('get_poems'))
    

@app.route('/get_genres')
def get_genre():
    return render_template('genres.html',
    genres=mongo.db.genres.find())
    

@app.route('/edit_genre/<genre_id>')
def edit_genre(genre_id):
    return render_template('editgenre.html',
    genre=mongo.db.genres.find_one({'_id': ObjectId(genre_id)}))


@app.route('/update_genre/<genre_id>', methods=['POST'])
def update_genre(genre_id):
    mongo.db.genres.update(
        {'_id': ObjectId(genre_id)},
        {'genre_name': request.form['genre_name']})
    return redirect(url_for('get_genre'))

  

@app.route('/delete_genre/<genre_id>')  
def delete_genre(genre_id):
    mongo.db.genres.remove({'_id': ObjectId(genre_id)})
    return redirect(url_for("get_genre"))
    

@app.route('/insert_genre', methods=['POST'])
def insert_genre():
    genres = mongo.db.genres
    genre_doc = {'genre_name': request.form['genre_name']}
    genres.insert_one(genre_doc)
    return redirect(url_for('get_genre'))
    

@app.route('/new_genre')
def new_genre():
    return render_template('addgenre.html')

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
