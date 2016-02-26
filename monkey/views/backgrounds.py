from os import path, listdir
from random import choice as random_choice

backgrounds = [None]


def load_backgrounds(app):
    p = path.join(path.join(app.config['BASE_DIR'], path.dirname(__file__)), '../static/images/')
    global backgrounds
    backgrounds = [f for f in listdir(p)]

    @app.context_processor
    def inject_background():
        # background = 'photo-1429734160945-4f85244d6a5a.jpg'
        background = random_choice(backgrounds)
        return dict(background=background)
