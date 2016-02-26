from flask_restless import APIManager
from monkey import app, db

manager = APIManager(app=app, flask_sqlalchemy_db=db)


def start_api(models):
    # Create API endpoints, which will be available at /api/<tablename> by
    # default. Allowed HTTP methods can be specified as well.
    for model in models:
        manager.create_api(model, methods=['GET', 'POST', 'DELETE'], url_prefix='/api/v1')
        # ...
