from unittest import TestCase

from app import app
from models import db, connect_db, User

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

        user = User(first_name="John", last_name="Smith", image_url="https://picsum.photos/id/433/300/300")
        db.session.add(user)
        db.session.commit()

        self.id = user.id


    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()


    def test_list_user(self):
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('John Smith', html)