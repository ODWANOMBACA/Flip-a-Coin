from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Flip-Coin'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Registering all blueprints
    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app