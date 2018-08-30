# app/routes.py: Home page route
from app import app1

@app1.route('/')
@app1.route('/index')
def index():
    return "Hello, World!"