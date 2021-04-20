from flask import Flask, request, Blueprint,jsonify,current_app

func1_blueprint = Blueprint('func1_blueprint', __name__)


@func1_blueprint.route('/')
def index():
    return 'Index hello.'
    