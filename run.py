import os

from monkey import create_app

if __name__ == '__main__':
    app = create_app(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.py'))
    app.run(debug=True, port=app.config['PORT'], host=app.config["HOST"])
# ---


