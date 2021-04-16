"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag
from seed import run_seed

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

app.config['SECRET_KEY'] = "keepthissecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

### Call 'run_seed()' if you want to reset the database with seed data from seed.py
### Uncomment the function below, run flask or reload app page.
### Comment out function again so as to not reset database with every page load.
#run_seed()

@app.route('/')
def list_recent_post():
    """Shows Recent Posts"""
    posts = Post.get_recent_10()
    return render_template('home_posts.html', posts=posts)

##########USERS

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


##########POSTS

@app.route('/users/<int:user_id>/posts/new')
def add_post_form(user_id):
    """Show new post form"""
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    # go to add post form
    return render_template("add_post.html", user=user, tags=tags)



@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def add_post(user_id):
    """Create post"""
    # collect post info
    title = request.form["title"]
    content = request.form["content"]

    tag_ids = [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    # Create new post instance
    new_post = Post(title=title, content=content, user_id=user_id, tags=tags)
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
    tags = Tag.query.all()
    # Renders post edit form
    return render_template("edit_post.html", post=post, tags=tags)



@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def update_post(post_id):
    """Post post info edits"""
    post = Post.query.get_or_404(post_id)
    # collect post info
    post.title = request.form["title"]
    post.content = request.form["content"]

    tag_ids = [int(num) for num in request.form.getlist("tags")]
    post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

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

##########TAGS

@app.route('/tags')
def list_all_tags():
    """Shows list of all tags"""
    tags = Tag.query.all()
    return render_template('all_tags.html', tags=tags)



@app.route('/tags/<int:tag_id>')
def show_tag_details(tag_id):
    """Show Posts"""
    tag = Tag.query.get_or_404(tag_id)

    # Renders tag details page
    return render_template("tag_details.html", tag=tag)



@app.route('/tags/new')
def create_tag_form():
    """Show create tag form"""
    # Renders tag details page
    posts = Post.query.all()
    return render_template("add_tag.html", posts=posts)



@app.route('/tags/new', methods=["POST"])
def create_tag():
    """Post tag to db"""
    name = request.form["name"]
    # Create new tag instance
    post_ids = [int(num) for num in request.form.getlist("posts")]
    posts = Post.query.filter(Post.id.in_(post_ids)).all()

    new_tag = Tag(name=name, posts=posts)

    # Commit updated post to db
    db.session.add(new_tag)
    db.session.commit()
    # Return to tag details page
    flash("Tag has been created", "alert-primary")
    return redirect(f"/tags/{new_tag.id}")



@app.route('/tags/<int:tag_id>/edit')
def edit_tag_form(tag_id):
    """Show edit form for tag"""
    tag = Tag.query.get_or_404(tag_id)
    posts = Post.query.all()
    # Renders tag edit form
    return render_template("edit_tag.html", tag=tag, posts=posts)



@app.route('/tags/<int:tag_id>/edit', methods=["POST"])
def edit_tag(tag_id):
    """Post tag info edits"""
    tag = Tag.query.get_or_404(tag_id)
    # collect tag info
    tag.name = request.form["name"]

    post_ids = [int(num) for num in request.form.getlist("posts")]
    tag.posts = Post.query.filter(Post.id.in_(post_ids)).all()

    # Commit updated tag to db
    db.session.add(tag)
    db.session.commit()
    # Return to tag details page
    flash("Tag has been updated", "alert-primary")
    return redirect(f"/tags/{tag_id}")



@app.route('/tags/<int:tag_id>/delete')
def delete_tag(tag_id):
    """Delete post"""
    tag = Tag.query.get_or_404(tag_id)
    # Delete from db
    db.session.delete(tag)
    db.session.commit()
    # Return to tags page
    flash("Tag has been deleted", "alert-danger")

    return redirect(f"/tags")



@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404