from bottle import *

# Index/Home page
# Copy these to create a new route
@route('/')
def index():
    return template(
        'pages/new/index.html', 
        username="Login", 
        title="Home", 
        description="Home Page", 
        menu={'screeners': [], 'sectors': []}
    )

# Test React
@route('/react')
def react():
    return template(
        'build/index.html', 
        username="Login", 
        title="Home", 
        description="Home Page", 
        menu={'screeners': [], 'sectors': []}
    )

# Serve dist folder
@route('/build/<filepath:path>')
def serve_dist_files(filepath):
    return static_file(filepath, root='build/')

# Serve static folder
@route('/<filepath:path>')
def serve_static_files(filepath):
    return static_file(filepath, root='static/')
    
run(reloader=True, host='localhost', port=8082)