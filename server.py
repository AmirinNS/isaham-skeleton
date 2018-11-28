from bottle import *

# Index/Home page
@route('/')
def index():
    return template(
        'index.html', 
        username="Login", 
        title="Home", 
        description="Home Page", 
        menu={'screeners': [], 'sectors': []}
    )

# Serve static folder
@route('/<filepath:path>')
def lib(filepath):
    return static_file(filepath, root='static/')
    
run(host='localhost', port=8082)