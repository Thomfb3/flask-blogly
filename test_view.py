from unittest import TestCase

from flask import Flask, request, render_template, redirect, flash, session
import datetime
from app import app
from models import db, User, Post, Tag, PostTag

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

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
        
        user = User(first_name="Tom", last_name="Smith", image_url="https://picsum.photos/id/433/300/300")

        db.session.add(user)
        db.session.commit()

        found_user = User.query.filter_by(first_name='Tom').first()
        self.id = found_user.id


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
            self.assertIn('Tom Smith', html)

    
    def test_list_details(self):
        """User details view"""
        with app.test_client() as client:
            resp = client.get(f"/users/{self.id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # User properties
            self.assertIn('Tom', html)
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
            self.assertIn('Tom', html)
            self.assertIn('Smith', html)
            self.assertIn('https://picsum.photos/id/433/300/300', html)


    def test_delete_user(self):
        """Delete this user"""
        with app.test_client() as client:
            resp = client.get(f"/users/{self.id}/delete")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 302)





class PostViewsTestCase(TestCase):
    """Tests for views for User."""

    def setUp(self):
        """Add sample User."""
        User.query.delete()
        Post.query.delete()

        user = User(first_name="John", last_name="Smith", image_url="https://picsum.photos/id/433/300/300")
        db.session.add(user)
        db.session.commit()

        found_user = User.query.filter_by(first_name='John').first()

        post = Post(title="Hi there, a new post", content="This is some test post content. It should be longer than 50 characters to test shorten content method.", created_at=datetime.datetime.utcnow(), user_id=found_user.id)
        db.session.add(post)
        db.session.commit()

        self.id = user.id
        self.post_id = post.id


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


    def test_delete_post(self):
        """Delete this post"""
        with app.test_client() as client:
            resp = client.get(f"/posts/{self.post_id}/delete")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 302)





class TagViewsTestCase(TestCase):
    """Tests for views for User."""

    def setUp(self):
        """Add sample User."""
        Tag.query.delete()
 
        tag = Tag(name="Cool")
       
        db.session.add(tag)
        db.session.commit()

        self.id = tag.id


    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()


    def test_all_tags(self):
        """All Tags view"""
        with app.test_client() as client:
            resp = client.get(f"/tags")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # page title
            self.assertIn('Cool', html)
            # User full name


    def test_tag_details(self):
        """Tags Details view"""
        with app.test_client() as client:
            resp = client.get(f"/tags/{self.id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # tag name
            self.assertIn('Cool', html)


    def test_edit_tag_form(self):
        """Edit Tags view"""
        with app.test_client() as client:
            resp = client.get(f"/tags/{self.id}/edit")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # tag name
            self.assertIn('Cool', html)


    def test_create_tag_form(self):
        """Create Tags view"""
        with app.test_client() as client:
            resp = client.get(f"/tags/new")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # tag name
            self.assertIn('Create', html)