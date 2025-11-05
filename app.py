from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, mundo!'

@app.route('/sobre')
def sobre():
    return "<h1>pagina info</h1>"

@app.route('/info')
def info():
    modulo = "css"
    aula = '7'
    return f"<h1>Modulo: {modulo}</h1><h1>Aula: {aula}</h1>"

@app.route('/bem-vindo')
def bem_vindo():
    modulo = "css"
    aula = '7'
    return f"<h1>Modulo: {modulo}</h1><h1>Aula: {aula}</h1>"

@app.route('/bem-vindo/<usuario>')
def bem_vindo_usuario(usuario):
    return f"<h1>Bem-vindo, {usuario}!</h1>"

@app.get("/bemvindo/<usuario>")
def bemvindo(usuario):
    return f"<h1>Bem-vindo, {usuario.capitalize()}!</h1>"

@app.get("/home")
def home():
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

