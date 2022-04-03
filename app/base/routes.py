from flask import render_template
from app.base import bp


@bp.route('/')
@bp.route('/index')
def index():
    user = {'username': 'Kangaroo'}
    return render_template('index.html', title='Home', user=user)
