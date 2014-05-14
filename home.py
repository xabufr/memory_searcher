from flask import Flask
app = Flask(__name__)

@app.route('/search')
def hello_world():
    return '<div>recherche!</div>'

@app.route('/')
def search():
    return '<div>Hello MADAFAKA!</div>'

if __name__ == '__main__':
    app.run()