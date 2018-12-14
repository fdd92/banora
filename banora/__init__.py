from flask import Flask, render_template
app = Flask(__name__)


def create_app():
    from . import index
    app.register_blueprint(index.bp)
    return app
