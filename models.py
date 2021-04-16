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

    # User Model Representation
    def __repr__(self):
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url} >"

    @property
    def full_name(self):
        """Return full name of user."""
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        """Return full name of user."""
        return f"{self.first_name} {self.last_name}"



class Post(db.Model):
    """Post Model"""
    __tablename__ = "posts"

    # Set time to eastern
    eastern = datetime.datetime.utcnow() + datetime.timedelta(hours= -4)
    
    # set the Post table columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=eastern)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Post Model Representation
    def __repr__(self):
        p = self
        return f"<Post id={p.id} title={p.title} content=text created_at={p.created_at} >"

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



class Tag(db.Model):
    """Tag Model"""
    __tablename__ = "tags"
    
    # set the Tag table columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    # Backref Posts to tags
    posts = db.relationship('Post', secondary="posts_tags", backref="tags")

    # Tag Model Representation
    def __repr__(self):
        t = self
        return f"<Tag id={t.id} name={t.name} >"

    @property
    def post_count(self):
        """Post Count"""
        post_count = len(self.posts)
        return post_count





class PostTag(db.Model):
    """Post Tags Model"""
    __tablename__ = "posts_tags"
    
    # set Post Tag table columns
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)