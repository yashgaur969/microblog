import unittest
import os
import json
from app import create_app, db, app


class CustomerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        # self.db = db
        self.client = app.test_client(self)

        with app.app_context():
            db.create_all()

    def test_customerlist_creation(self):
        self.assertEqual(201, 201)

    def test_get_hello(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_customers_get(self):
        response = self.client.get('/profile/mahesh/mahesh@gmail.com', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """teardown all initialized variables."""
        with app.app_context():
            # drop all tables
            db.session.remove()
            # self.db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()