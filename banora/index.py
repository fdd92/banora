from flask import Blueprint, render_template
from banora.tool import json_return

bp = Blueprint('auth', __name__)


@bp.route('/hello/<name>', methods=['GET'])
def hello_world(name):
    return render_template('index.html', name=name)


@bp.route('/test')
@json_return
def json_test():
    return [{'asdf': "ecx"}, "asdfa", {'asdf': 'asdf'}]
