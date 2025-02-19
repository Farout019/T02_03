from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)  # Permitir peticiones de otros orígenes durante el desarrollo

# Endpoint de la API
@app.route('/api/saludo')
def saludo():
    return jsonify({"mensaje": "PRUEBA"})

# Ruta para servir la aplicación React en producción
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
