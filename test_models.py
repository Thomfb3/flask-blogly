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


class UserModelTestCase(TestCase):
    """Tests for model for Users."""

    def setUp(self): 
        """Clean up any existing users."""
        User.query.delete()


    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()


    def test_user_properties(self):
        user = User(first_name="John", last_name="Smith", image_url="https://picsum.photos/id/433/300/300")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Smith")
        self.assertEqual(user.image_url, "https://picsum.photos/id/433/300/300")
        self.assertEqual(user.full_name, "John Smith")


    def test_get_full_name(self):
        user_two = User(first_name="Bob", last_name="Smithen", image_url="https://picsum.photos/id/433/300/300")
        self.assertEqual(user_two.get_full_name(), "Bob Smithen")



class PostModelTestCase(TestCase):
    """Tests for model for Users."""

    def setUp(self): 
        """Clean up any existing users."""
        Post.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()


    def test_post_properties(self):
        user = User(first_name="John", last_name="Smith", image_url="https://picsum.photos/id/433/300/300")
        
        post = Post(title="Hi there, here's a new post", content="This is some test post content. It should be longer than 50 characters to test shorten content method.", user_id=1)
        
        self.assertEqual(post.user_id, 1)
        self.assertEqual(post.title, "Hi there, here's a new post")
        self.assertEqual(post.content, "This is some test post content. It should be longer than 50 characters to test shorten content method.")
        self.assertNotEqual(post.short_content, "This is some test post content. It should be longer than 50 characters to test shorten content method.")



class TagModelTestCase(TestCase):
    """Tests for model for Users."""

    def setUp(self): 
        """Clean up any existing users."""
        Tag.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()


    def test_tag_properties(self):
        tag = Tag(name="Cool")
        self.assertEqual(tag.name, "Cool")
        