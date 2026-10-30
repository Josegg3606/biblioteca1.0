from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", titulo="home", mensaje="Bienvenido a la pagina de inicio")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")




if __name__ == "__main__":
    app.run(debug=True,port=5050)