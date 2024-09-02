from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

biodiversidad = [
    {'id': 0, 'tipo': 'fauna', 'nombre': 'Oryctolagus cuniculus'},
    {'id': 1, 'tipo': 'fauna', 'nombre': 'Columba corensis'},
    {'id': 2, 'tipo': 'fauna', 'nombre': 'Lachesis muta'},
    {'id': 10, 'tipo': 'flora', 'nombre': 'Espeletia pycnophylla',},
    {'id': 11, 'tipo': 'flora', 'nombre': 'Eryngium andicola'},
    {'id': 12, 'tipo': 'flora', 'nombre': 'Senecio laevis'},
],
@app.route('/', methods=['GET'])
def principal():
    return "Estoy funcionando"

@app.route('/api/v1/biodiversidad/all', methods=['GET'])
def datos_biodiversidad():
    return jsonify(biodiversidad)
if __name__ == '__main__':
    app.run(port=5000)   

if __name__ == '__main__':
    app.run()
