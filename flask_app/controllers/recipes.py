from crypt import methods
import datetime
from flask_app import app
from flask import render_template, redirect, request, session, flash 
from flask_app.models import recipe, user


@app.route('/new_recipe')
def new_recipe():
    return render_template("add_recipe.html")

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect('/new_recipe')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_30': request.form['under_30'],
        'date_made': request.form['date_made'],
        'user_id': session['user_id']
    }
    
    recipe.Recipe.save(data)
    
    return redirect('/dashboard')

@app.route('/view_recipe/<int:id>')
def view_recipe(id):
    data = {'id':id}
    this_recipe = recipe.Recipe.get_recipe_info(data)
    user_data = {'id': session['user_id']}
    this_user = user.User.get_all_by_id(user_data)
    

    return render_template('recipe.html', this_recipe = this_recipe, user = this_user)

@app.route('/edit_recipe/<int:id>')
def edit_recipe(id):
    data = {'id':id}
    this_recipe = recipe.Recipe.get_recipe_info(data)
    return render_template('edit_recipe.html', this_recipe = this_recipe)

@app.route('/update_recipe', methods=['POST'])
def update_recipe():
    data = {
        'id' : request.form['id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_30': request.form['under_30'],
        'date_made': request.form['date_made'],
    }
    recipe.Recipe.update(data)
    return redirect('/dashboard')



    