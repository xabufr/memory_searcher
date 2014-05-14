from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<label>Entrer  le nom du fichier</label><input type="text" style="width:150px"><input type="submit" value="Envoi">'

if __name__ == '__main__':
    app.run()