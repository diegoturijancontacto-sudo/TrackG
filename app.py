"""
Flask web application para TrackG - Seguimiento de Ejercicios.
Servidor web que sirve la interfaz HTML/JS para el seguimiento de ejercicios.
"""

from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    """Página principal de la aplicación web."""
    return render_template('index.html')


@app.route('/api/exercises')
def get_exercises():
    """API endpoint que devuelve la lista de ejercicios disponibles."""
    exercises = {
        "1": "Bicep Curl",
        "2": "Shoulder Press",
        "3": "Lateral Raise",
        "4": "Front Raise",
        "5": "Hammer Curl",
        "6": "Tricep Extension"
    }
    return jsonify(exercises)


if __name__ == '__main__':
    print("=== TrackG - Aplicación Web de Seguimiento de Ejercicios ===")
    print("\nAbriendo servidor web en http://localhost:5000")
    print("Presiona Ctrl+C para detener el servidor\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
