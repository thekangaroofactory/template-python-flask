from flask import Flask


def create_app():

    app = Flask(__name__)

    # Configurations
    app.config.from_pyfile('../config.py')

    # Check config option
    if app.config['KANGAROO_ID'] == 'KANGAROO_ID':
        print("Config OK")

    # Base Component Blueprint
    from app.base import bp as base_bp
    app.register_blueprint(base_bp)

    return app
