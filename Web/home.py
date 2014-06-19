from flask import Flask
app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return app.make_response(open('static/memory_search.html').read())

if __name__ == '__main__':
    app.run()
