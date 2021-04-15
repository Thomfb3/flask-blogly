from unittest import TestCase

import datetime
from app import app
from models import db, User, Post

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = True

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()



class UserViewsTestCase(TestCase):
    """Tests for views for User."""

    def setUp(self):
        """Add sample User."""
        User.query.delete()

        user = User(first_name="John", last_name="Smith", image_url="https://picsum.photos/id/433/300/300")

        db.session.add(user)
        db.session.commit()


        self.id = user.id


    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()


    def test_list_user(self):
        """Test user in list"""
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)
            # User name
            self.assertEqual(resp.status_code, 200)
            self.assertIn('John Smith', html)

    
    def test_list_details(self):
        """User details view"""
        with app.test_client() as client:
            resp = client.get(f"/users/{self.id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # User properties
            self.assertIn('John', html)
            self.assertIn('Smith', html)
            self.assertIn('https://picsum.photos/id/433/300/300', html)


    def test_add_user(self):
        """Add user view"""
        with app.test_client() as client:
            resp = client.get(f"/users/new")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # User properties
            self.assertIn('Create New User', html)


    def test_edit_user(self):
        """Edit user view"""
        with app.test_client() as client:
            resp = client.get(f"/users/{self.id}/edit")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # User properties
            self.assertIn('John', html)
            self.assertIn('Smith', html)
            self.assertIn('https://picsum.photos/id/433/300/300', html)

    





class PostViewsTestCase(TestCase):
    """Tests for views for User."""

    def setUp(self):
        """Add sample User."""
        User.query.delete()
        Post.query.delete()

        user = User(first_name="John", last_name="Smith", image_url="https://picsum.photos/id/433/300/300")
        db.session.add(user)

        post = Post(title="Hi there, a new post", content="This is some test post content. It should be longer than 50 characters to test shorten content method.", created_at=datetime.datetime.utcnow(), user_id=user.id)
        db.session.add(post)
        
        db.session.commit()

        self.id = user.id


    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()



    def test_recent_posts(self):
        """Recent posts view"""
        with app.test_client() as client:
            resp = client.get(f"/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # page title
            self.assertIn('Recent Posts', html)
            # User full name
            self.assertIn('John', html)
            # User image
            self.assertIn('https://picsum.photos/id/433/300/300', html)
            # Post tile
            self.assertIn("Hi there, a new post", html)
            # Post Short Content
            self.assertIn("This is some test", html)