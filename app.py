from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, mundo!'
@app.route('/sobre')
def sobre():
    return "<h1>pagina info<h1>"
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