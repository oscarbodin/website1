from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from os import path
from flask_login import LoginManager

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'asdasd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists(f'instance/ + {DB_NAME}'):
        with app.app_context():
            db.create_all()
