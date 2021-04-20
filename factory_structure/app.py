from flask import Flask
from api.func1 import func1_blueprint
from flask_mail import Mail, Message

def create_app():
    app = Flask(__name__)
    app.register_blueprint(func1_blueprint)
    
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = ''
    app.config['MAIL_PASSWORD'] = ''
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail= Mail(app)
    

    return app

    
