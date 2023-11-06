from flask import Flask, render_template, request, redirect,url_for,jsonify
from homepage_controller import *


app = Flask(__name__,template_folder='template')
application = app

@app.route('/', methods=['GET','POST'])
def homepage():
    return render_template('public/index.html',datos=showProductInPage())


@app.route('/detallecompra/<int:prod_id>', methods=['GET', 'POST'])
def verDetalles(prod_id):
    if request.method == 'GET':
        resultado = detalleprod(prod_id)
        if resultado:
            return render_template('public/detalleproducto.html', detallesProducto = resultado)
        else:
             return render_template('public/index.html')
    return redirect(url_for('homepage'))


@app.route('/comprar/<int:prod_id>', methods=['GET', 'POST'])
def hacerCompra(prod_id):
    if request.method == 'GET':
        resultado = detalleprod(prod_id)
        if resultado:
            return render_template('public/comprar.html', detallesProducto = resultado)
        else:
             return render_template('public/index.html')
    return redirect(url_for('homepage'))


@app.route('/comprar/', methods=['POST'])
def guardarUsuario():
    if request.method=='POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        email = request.form['email']

        total = request.form['total']
        idprod = request.form['idprod']
        cantidad=request.form['cant']
        stockactual = request.form['stockactual']

    if(cedula !=""):
        resultado=registrarUsuario(cedula,nombre,apellido,telefono,direccion,email,total,idprod,cantidad,stockactual)
    if(resultado==1):
        return render_template('public/success.html')
    else:
        print("Hubo un error raro")
    

@app.route('/finalizarcompra/<int:prod_id>', methods=['GET','POST'])
def mostrarFrmCompra(prod_id):
    if request.method == 'POST':
        resultado = detalleprod(prod_id)
        cant_art = request.form['cantidad']
        valor_numerico = int(cant_art)
        if resultado:
             return render_template('public/comprar.html', detallesProducto = resultado,cantidad = valor_numerico)
        else:
             return render_template('public/index.html')
    return redirect(url_for('homepage')) 
    
   


#esto debe estar de ultimo y es necesario
if __name__ == "__main__":
    app.run(debug=True, port=8000)