from flask import request, Flask
from flask.ext.login import LoginManager
from models import UserModel

app = Flask(__name__)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    """
        required by flask_login
        :param user_id: Type: Int
    """
    """
        It should return None (not raise an exception)
        if the ID is not valid.
        (In that case, the ID will manually be removed from the session
         and processing will continue.)
         :param user_id: primary key
    """
    return UserModel.get(user_id)


def create_app(config_file):
    # load config
    app.config.from_pyfile(config_file)

    from views.backgrounds import load_backgrounds
    load_backgrounds(app)

    # setup db
    from database import db
    db.init_app(app)

    # setup login
    login_manager.init_app(app)

    # login_manager.setup_app(app)

    from monkey.views import index_view, login_view

    for bp in [login_view, index_view]:
        app.register_blueprint(bp)

    # init all
    with app.app_context():
        db.create_all()
        import api

        api.start_api([UserModel])
        UserModel.initialize()

    return app


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

# ---
