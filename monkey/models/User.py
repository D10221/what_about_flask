from flask.ext.login import UserMixin


from monkey.database import db

Column = db.Column
Integer = db.Integer
String = db.String
Base = db.Model
Unicode = db.Unicode


class UserModel(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    username = Column(Unicode)
    password = Column(Unicode)

    def __init__(self, name=None, email=None, username=None, password=None):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name

    def is_authenticated(self):
        """
            Returns True if the user is authenticated,
            i.e. they have provided valid credentials.
            Only authenticated users
            will fulfill the criteria of login_required.
        :return:
        """
        return True

    def is_active(self):
        """
            Returns True if this is an active user,
            in addition to being authenticated,
            they also have activated their account,
            not been suspended,
            or any condition your application has for rejecting an account.
            Inactive accounts may not log in (without being forced of course).
        :return:
        """
        return True

    def is_anonymous(self):
        """
            Returns True if this is an anonymous user.
            (Actual users should return False instead.)
        :return:
        """
        return False

    def get_id(self):
        """
            Returns a unicode that uniquely identifies this user,
            and can be used to load the user from the user_loader callback.
            Note that this must be a unicode
            - if the ID is natively an int or some other type,
             you will need to convert it to unicode.
        :return:
        """
        return str(self.id).encode("utf-8").decode("utf-8")

    @staticmethod
    def initialize():
        if db.session.query(UserModel).filter(UserModel.name == 'Dan').first() is None:
            db.session.add(UserModel(
                name='Dan',
                email='dan@mail',
                username='dan',
                password='1234'))
            db.session.commit()

    @staticmethod
    def get(user_id):
        return db.session.query(UserModel).filter(UserModel.id == user_id).first()

