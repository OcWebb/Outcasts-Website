from flask import render_template
from app_package import app


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('base.html')
