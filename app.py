from flask import Flask, render_template, request, redirect,url_for,jsonify
from homepage_controller import *
from flask_mail import Mail, Message
import os


app = Flask(__name__,template_folder='template')
application = app

#Configuracion del Correo Electrinico
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'  # Servidor de correo saliente (SMTP)
app.config['MAIL_PORT'] = 587  # Puerto SMTP
app.config['MAIL_USE_TLS'] = True  # Usar TLS
app.config['MAIL_USERNAME'] = 'cabascarlosandres@outlook.com'  # Tu dirección de correo electrónico
app.config['MAIL_PASSWORD'] = mypassemail  # Tu contraseña

mail = Mail(app)


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
        msg=Message('Compra Exitosa, su articulo llegará pronto', sender='cabascarlosandres@outlook.com',recipients=[email])
        msg.body="Gracias por comprar nuestros articulos, espero que sean de agrado y puedan disfruta de ello. Su articulo llegará a su domicilio"

        # Adjuntar una imagen al correo (asegúrate de que la imagen exista en la carpeta estática de tu aplicación)
        with app.open_resource(os.path.join(app.root_path, 'static', 'gracias.jpg')) as fp:
            msg.attach('gracias.jpg', 'image/jpeg', fp.read())

        #envia el correo...y listo
        mail.send(msg)

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