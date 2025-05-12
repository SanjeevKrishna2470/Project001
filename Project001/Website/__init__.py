from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
DB_NAME="database.db"#db is the database object


def createApp():
    app= Flask(__name__)
    app.config['SECRET_KEY']='sdscdcefefdcxcsfuckinghell'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'#specifying where the database is located to the main program
    db.init_app(app) #initializing the database and connecting it to the flask app
    login_manager =LoginManager()
    login_manager.login_view ='auth.login' #route name for unauthorized users. It's the place where users are redirected if they try to access protected pages while logged out.
    login_manager.init_app(app) #connects to flask app

    @login_manager.user_loader
    def load_user(id): #basically used for 'verification'. Despite the database connection being established, there is a need to manage user sessions. It is meant to validate user on each request. Creates a fresh instance each time. 
        return User.query.get(int(id))
    from .views import views #the blueprints have to be imported in order to let the app know of them
    from .auth import  auth
    from .models import User,Note
    from os import path
    
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/') #prefix is only / and does not need any other word that is not specified
    def create_Database(app):
        if not path.exists('Website'+DB_NAME):
            with app.app_context():
              db.create_all()
              print("Created Database")
    create_Database(app)
    
    return app
   