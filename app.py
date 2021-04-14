"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "keepthissecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
#db.create_all()


@app.route('/')
def list_users():
    """Shows list of users"""
    users = User.query.all()
    #return render_template('users.html', users=users)
    return redirect('/users')


@app.route('/users')
def list_all_users():
    """Shows list of all users"""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('all_users.html', users=users)


@app.route('/users/new')
def create_user_form():  
    return render_template('add_user.html')


@app.route('/users/new', methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    image_url = image_url if image_url else None
    
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f'/users/{new_user.id}')



@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show pet details about a single pet"""
    user = User.query.get_or_404(user_id)
    return render_template("user_details.html", user=user)



@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Show pet details about a single pet"""
    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_user(user_id):
    """Show pet details about a single pet"""
    found_user = User.query.get_or_404(user_id)

    found_user.first_name = request.form["first_name"]
    found_user.last_name = request.form["last_name"]
    found_user.image_url = request.form["image_url"]

    db.session.add(found_user)
    db.session.commit()

    flash("User has been updated", "alert-primary")
    return redirect(f'/users/{found_user.id}')



@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    """Show pet details about a single pet"""
    found_user = User.query.get_or_404(user_id)

    db.session.delete(found_user)
    db.session.commit()

    flash("User has been deleted", "alert-danger")
    return redirect(f'/users')