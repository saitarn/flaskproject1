# app/routes.py: default route page
from app import app1

@app1.route('/')
@app1.route('/index')
def index():
    return "Hello, World!"