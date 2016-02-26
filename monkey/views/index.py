from flask import Blueprint, render_template,session

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def show():

    return render_template('index.html', **{
        'x': 1,
        # 'current_user': current_user
    })
