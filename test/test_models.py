import os

from unittest import TestCase

from sqlalchemy.orm import Query

from monkey import create_app, UserModel

from flask_sqlalchemy_session import current_session


def populate_db():
    pass


def set_app():
    pass


# noinspection PyPep8Naming,PyMethodMayBeStatic
class TestUserModel(TestCase):
    def setUp(self):
        print 'Setup!'
        # Query(UserModel).add_entity(UserModel('joe', 'joe@mail'))
        self.app = create_app(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'flask_config.py'))
        print dir(UserModel.query)
        UserModel.add_entity(UserModel(name='joe', email='joe@mail'))
        print UserModel.query.all()
        """
        Creates a new database for the unit test to use
        """
        # ---

    # ---

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        print 'tearDown'
        # ---

        # ---

    # ---

    def test_user(self):
        print 'testing ... '

        user = current_session.query(UserModel).get(1)
        assert user in UserModel.query.all()
