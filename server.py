from flask import Flask, request, jsonify
from logic.MemorySearcher import MemorySearcher
import json
app = Flask(__name__, static_url_path='')
searcher = MemorySearcher()

@app.route('/')
def index():
    return app.make_response(open('static/memory_search.html').read())

@app.route('/memory', methods=['POST'])
def memory():
    data = request.json

    if 'search' in data:
        result = searcher.search_globally(data['search'], ['metadata.title', 'metadata.author', 'metadata.date'])
    else:
        result = searcher.search_on_fields(data);
    return app.make_response(json.dumps(MemorySearcher.pretify(result)))

@app.route('/memory/<id>')
def memoryFromId(id):
    result = searcher.get(id)
    return app.make_response(json.dumps(result['_source']))

if __name__ == '__main__':
    app.run()
