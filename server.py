from flask import Flask
app = Flask(__name__)

@app.get('/')
def index():
    return '''
    <a href="resume">Resume</a>
    -
    <a href="contact">Contact</a>
    '''
    
@app.get('/resume')
def resume():
    return 'Lorem ipsum etc'