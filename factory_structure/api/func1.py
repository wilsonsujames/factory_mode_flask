from flask import Flask, request, Blueprint,jsonify,current_app
from flask_mail import Mail, Message

func1_blueprint = Blueprint('func1_blueprint', __name__)


@func1_blueprint.route('/')
def index():
    msg = Message('Hello', sender = '*****@gmail.com', recipients = [ '*****@gmail.com'])
    msg.body = 'hello hello hello'
    with current_app.app_context():
        mail = Mail()
        mail.send(msg)
    
    
    return 'Index hello.'
    
