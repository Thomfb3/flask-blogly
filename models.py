"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


# MODELS GO HERE 
class User(db.Model):
    """User Model"""
    __tablename__ = "users"

    # Set the User columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=False, default="https://picsum.photos/id/433/300/300")

    # Backreference all posts for user and cascade delete posts
    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    # Representation
    def __repr__(self):
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}"

    @property
    def full_name(self):
        """Return full name of user."""
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        """Return full name of user."""
        return f"{self.first_name} {self.last_name}"


    


class Post(db.Model):
    """User Model"""
    __tablename__ = "posts"

    # Set time to eastern
    eastern = datetime.datetime.utcnow() + datetime.timedelta(hours= -4)
    
    # set the Post table columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=eastern)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Representation
    def __repr__(self):
        u = self
        return f"<Post id={u.id} title={u.title} content=text created_at={u.created_at}"

    @property
    def date(self):
        """Make readable date from created_at timestamp"""
        created_timestamp = self.created_at
        return created_timestamp.strftime("%b %d, %Y - %I:%M %p ")
    
    @property
    def short_content(self):
        """Make a short version of the post content for previews"""
        short_content = self.content[0:50] + "..."
        return short_content

    def get_recent_10():
        posts = Post.query.order_by(Post.id.desc())
        if posts.count() > 10:
            posts = posts[:10]
        return posts


