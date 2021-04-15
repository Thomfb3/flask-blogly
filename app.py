"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "keepthissecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
# db.drop_all()
# db.create_all()

@app.route('/')
def list_recent_post():
    """Shows Recent Posts"""
    posts = Post.get_recent_10()
    return render_template('home_posts.html', posts=posts)


@app.route('/users')
def list_all_users():
    """Shows list of all users"""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('all_users.html', users=users)



@app.route('/users/new')
def create_user_form():  
    """Show create user form"""
    return render_template('add_user.html')



@app.route('/users/new', methods=["POST"])
def create_user():
    """Create a new user"""
    # Create user form
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    image_url = image_url if image_url else None
    # Apply form data to User object
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    # Commit to database
    db.session.add(new_user)
    db.session.commit()
    # Redirect to user details page
    return redirect(f"/users/{new_user.id}")



@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details for user"""
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter(Post.user_id == user_id).all()
    # Redirect to user details page
    return render_template("user_details.html", user=user, posts=posts)



@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Show edit form for user"""
    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)



@app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_user(user_id):
    """Post user info edits"""
    user = User.query.get_or_404(user_id)
    # collect user data
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]
    # commit edits
    db.session.add(user)
    db.session.commit()
    # redirect to user page
    flash("User has been updated", "alert-primary")
    return redirect(f"/users/{user.id}")



@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    """Delete user"""
    found_user = User.query.get_or_404(user_id)
    # Delete user from db
    db.session.delete(found_user)
    db.session.commit()
    # Go to all users page
    flash("User has been deleted", "alert-danger")
    return redirect(f'/users')



@app.route('/users/<int:user_id>/posts/new')
def add_post_form(user_id):
    """Show new post form"""
    user = User.query.get_or_404(user_id)
    # go to add post form
    return render_template("add_post.html", user=user)



@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def add_post(user_id):
    """Create post"""
    # collect post info
    title = request.form["title"]
    content = request.form["content"]
    # Create new post instance
    new_post = Post(title=title, content=content, user_id=user_id)
    # Commit post to db
    db.session.add(new_post)
    db.session.commit()
    # Return to user page
    flash("Post created", "alert-primary")
    return redirect(f"/users/{user_id}")



@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """Show Posts"""
    post = Post.query.get_or_404(post_id)
    # Renders post content
    return render_template("post_content.html", post=post)



@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    """Show edit form for post"""
    post = Post.query.get_or_404(post_id)
    # Renders post edit form
    return render_template("edit_post.html", post=post)



@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def update_post(post_id):
    """Post post info edits"""
    post = Post.query.get_or_404(post_id)
    # collect post info
    post.title = request.form["title"]
    post.content = request.form["content"]
    # Commit updated post to db
    db.session.add(post)
    db.session.commit()
    # Return to post details page
    flash("Post has been updated", "alert-primary")
    return redirect(f"/posts/{post_id}")



@app.route('/posts/<int:post_id>/delete')
def delete_post(post_id):
    """Delete post"""
    post = Post.query.get_or_404(post_id)
    user_id = post.user.id
    # Delete from db
    db.session.delete(post)
    db.session.commit()
    # Return to users page
    flash("Post has been deleted", "alert-danger")

    return redirect(f"/users/{user_id}")

@app.route('/posts/all')
def all_posts():
    """Show edit form for post"""
    posts = Post.query.order_by(Post.id.desc()).all()
    # Renders post edit form
    return render_template("all_posts.html", posts=posts)



@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404