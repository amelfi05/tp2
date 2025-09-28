from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    diccionario = {
        "nombre": "Rally MTB 2025",
        "organizador": "Club Social y Deportivo Unidos por el Deporte",
        "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km realizada por primera vez en la ciudad de Tandil, Buenos Aires. Inscripciones abiertas hasta el 15 de Octubre de 2025.",
        "fecha": "24 de Octubre de 2025",
        "horario": "8am",
        "lugar": "Tandil, Buenos Aires",
        "tipo_carrera": "MTB rural",
        "modalidad_costo": {1: {"nombre": "Corta" ,"valor": "100"},
        2: {"nombre": "Larga" ,"valor": "200"}},
        "Auspiciantes": ["ausp1","ausp2"]
    }

    return render_template("index.html", info=diccionario)

# Ruta de inscripción
@app.route("/registration")
def registro():
    return render_template("registration.html")

if __name__ == "__main__":
    app.run('localhost', port=5100, debug=True)
