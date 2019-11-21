from yoda2 import app

@app.route('/')
@app.route('/index')
def index( ):
    return 'Olá Mundão 2'
