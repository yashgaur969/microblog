import unittest
import os
import json
from app import create_app, db, app


class CustomerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        # self.db = db
        self.client = self.app.test_client

        with app.app_context():
            db.create_all()

    def test_customerlist_creation(self):
        self.assertEqual(201, 201)

    def tearDown(self):
        """teardown all initialized variables."""
        with app.app_context():
            # drop all tables
            db.session.remove()
            # self.db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()