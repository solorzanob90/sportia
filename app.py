from flask import Flask, render_template, request, redirect,url_for,jsonify,send_from_directory
from homepage_controller import *
from flask_mail import Mail, Message
import os
from PIL import Image, ImageDraw, ImageFont
from crud_controller import *
from login import *

app = Flask(__name__,template_folder='template')
application = app

#Configuracion del Correo Electronico
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'  # Servidor de correo saliente (SMTP)
app.config['MAIL_PORT'] = 587  # Puerto SMTP
app.config['MAIL_USE_TLS'] = True  # Usar TLS
app.config['MAIL_USERNAME'] = 'cabascarlosandres@outlook.com'  # Tu dirección de correo electrónico
app.config['MAIL_PASSWORD'] = "C#arles1990"  # Tu contraseña

mail = Mail(app)
########################################
#Aqui genero una factura en una imagen creada con Pillow
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/verificarusuario/', methods=['POST'])
def verificarusuario():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        resultado=verificaradmin(username, password)

    if (resultado):
        
        return render_template('public/paginaadmin.html', resultado=resultado)
    
    else: 
        print("Credenciales Incorrectas")


@app.route('/login', methods=['GET', 'POST'])
def login():
         
    return render_template('public/login.html')


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

        #creo una imagen con los datos de la compra
        facturaimg = Image.new('RGB',(450,400),color=(255,255,255))
        crearImgFactura = ImageDraw.Draw(facturaimg)
        tipoDeLetra = ImageFont.load_default()

        #datos del usuario que se imprimiran en la imagen
        crearImgFactura.text((10,10), f'DETALLE DE COMPRA',font=ImageFont.truetype("ARLRDBD.TTF",14),fill=(0,0,0),align='left',spacing=4)
        crearImgFactura.text((250,10), f'N. Factura: {id_pedido}',font=ImageFont.truetype("ARLRDBD.TTF",12),fill=(0,0,0),align='left',spacing=4)

        crearImgFactura.text((10,50), f'Nombre: {nombre}',font=ImageFont.truetype("Roboto-Regular.ttf",12),fill=(0,0,0),align='left',spacing=4)
        crearImgFactura.text((10,70), f'Apellido: {apellido}',font=ImageFont.truetype("Roboto-Regular.ttf",12),fill=(0,0,0),align='left',spacing=4)
        crearImgFactura.text((10,90), f'Domicilio: {direccion}',font=ImageFont.truetype("Roboto-Regular.ttf",12),fill=(0,0,0),align='left',spacing=4)
        crearImgFactura.text((10,120), f'---------------------------------------------------------------------------------------',font=tipoDeLetra,fill=(0,0,0),align='left',spacing=4)
       
        crearImgFactura.text((15,150), f'TOTAL PAGO: {total}',font=ImageFont.truetype("ARLRDBD.TTF",20),fill=(0,0,0),align='left',spacing=4)
        crearImgFactura.text((10,330), f'N. Guia: {random.randint(000000000000,999999999999)}',font=ImageFont.truetype("Roboto-Regular.ttf",18),fill=(0,0,0))
        crearImgFactura.text((10,300), f'SPORTIA: Tu tienda Deportiva',font=ImageFont.truetype("unispace bd.ttf",14),fill=(0,0,0))


        #creo la carpeta donde se guardara la imagen primero
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        #guarda la imagen en el directorio de subidas
        image_path = os.path.join(app.config['UPLOAD_FOLDER'],'user_data.png')
        facturaimg.save(image_path)


        msg=Message('Compra Exitosa, su articulo llegará pronto', sender='cabascarlosandres@outlook.com',recipients=[email])
        msg.body=f"Gracias por comprar nuestros articulos, espero que sean de agrado y puedan disfruta de ello. Su articulo llegará a su domicilio, puede ver el número de guia en la imagen adjunta y consultarla en la pagina de Servientrega en el link siguiente: https://www.servientrega.com/wps/portal/rastreo-envio/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziTS08TTwMTAz93f1cTAwCg5yMfP0MHT2NPQ30w8EKDHAARwP9KGL041EQhd_4cP0oPFYYOfoaQRXgMcNLPyo9Jz8J4l3HvCRji3T9qKLUtNSi1CK90iKgcEZJSUGxlaqBqkF5ebleUmZeul5yfq6qATYNGfnFJfoRyOr0C3JDIwyyTHPKfBwVASgvW-o!/dz/d5/L2dBISEvZ0FBIS9nQSEh/"

        # Adjuntar una imagen al correo (asegúrate de que la imagen exista en la carpeta estática de tu aplicación)
        #with app.open_resource(os.path.join(app.root_path, 'static', 'gracias.jpg')) as fp:
        #    msg.attach('gracias.jpg', 'image/jpeg', fp.read())

        #Adjunta la imagen creada con Pillow al correo
        with app.open_resource(image_path) as fp:
            msg.attach('user_data.png','image/png',fp.read())

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
    
   #___________________________________________CRUD DE PRODUCTOS_____________________________________________________

msg  =''
tipo =''


#Creando mi decorador para el home, el cual retornara la Lista de Carros
@app.route('/paginaadmin', methods=['GET','POST'])
def inicioAdmin():
    return render_template('public/paginaadmin.html', resultado = listaProductos())


#RUTAS
@app.route('/registrar-producto', methods=['GET','POST'])
def addProducto():
    return render_template('public/addProducto.html')


@app.route('/ver-detalles-del-producto/<int:idProd>', methods=['GET', 'POST'])
def viewDetalleProducto(idProd):
    msg =''
    if request.method == 'GET':
        resultData = detallesdelProducto(idProd) #Funcion que almacena los detalles del carro
        
        if resultData:
            return render_template('public/vistaProducto.html', infoProd = resultData, msg='Detalles del Producto', tipo=1)
        else:
            return render_template('public/paginaadmin.html', msg='No existe el Producto', tipo=1)
    return redirect(url_for('inicio'))

@app.route('/producto', methods=['POST'])
def formAddProducto():
    if request.method == 'POST':
        nombre               = request.form['nombre']
        descripcion          = request.form['descripcion']
        marca                = request.form['marca']
        precio               = request.form['precio']
        stock                = request.form['stock']
        
        
        
        if(request.files['imagen'] !=''):
            file     = request.files['imagen'] #recibiendo el archivo
            nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
            resultData = registrarProducto(nombre,descripcion, marca,precio,stock, nuevoNombreFile)
            if(resultData ==1):
                return render_template('public/paginaadmin.html', resultado = listaProductos(), msg='El Registro fue un éxito', tipo=1)
            else:
                return render_template('public/paginaadmin.html', msg = 'Metodo HTTP incorrecto', tipo=1)   
        else:
            return render_template('public/paginaadmin.html', msg = 'Debe cargar una foto', tipo=1)
        
@app.route('/form-update-producto/<int:id>', methods=['GET','POST'])
def formViewUpdate(id):
    if request.method == 'GET':
        resultData = updateProductos(id)
        if resultData:
            return render_template('public/update.html',  dataInfo = resultData)
        else:
            return render_template('public/paginaadmin.html', miData = listaProductos(), msg='No existe el carro', tipo= 1)
    else:
        return render_template('public/paginaadmin.html', miData = listaProductos(), msg = 'Metodo HTTP incorrecto', tipo=1)          
 

@app.route('/actualizar-producto/<int:idProd>', methods=['POST'])
def  formActualizarProducto(idProd):
    if request.method == 'POST':
        nombre               = request.form['nombre']
        descripcion          = request.form['descripcion']
        marca                = request.form['marca']
        precio               = request.form['precio']
        stock                = request.form['stock']
        
        #Script para recibir el archivo (foto)
        if(request.files['imagen']):
            file     = request.files['imagen']
            fotoForm = recibeFoto(file)
            resultData = recibeActualizarProductos(nombre,descripcion, marca,precio,stock, fotoForm, idProd)
        else:
            fotoCarro  ='imagen-vacia.jpg'
            resultData = recibeActualizarProductos(nombre,descripcion, marca,precio,stock, fotoCarro, idProd)

        if(resultData ==1):
            return render_template('public/paginaadmin.html', resultado = listaProductos(), msg='Datos del carro actualizados', tipo=1)
        else:
            msg ='No se actualizo el registro'
            return render_template('public/paginaadmin.html', resultado = listaProductos(), msg='No se pudo actualizar', tipo=1)
        
@app.route('/borrar-producto', methods=['GET', 'POST'])
def formViewBorrarProducto():
    if request.method == 'POST':
        idProd         = request.form['id_producto']
        nombre_imagen      = request.form['nombre_imagen']
        resultData      = eliminarProducto(idProd, nombre_imagen)

        if resultData ==1:
            #Nota: retorno solo un json y no una vista para evitar refescar la vista
            return jsonify([1])
            #return jsonify(["respuesta", 1])
        else: 
            return jsonify([0])
        
        
@app.route('/paginaadmin/', methods=['POST'])
def irAPaginaAdmin():
    resultado=listaProductos()

    if (resultado):
        
        return render_template('public/paginaadmin.html', resultado=resultado)

#_____________________________________________________________________________________________________________________
#esto debe estar de ultimo y es necesario
if __name__ == "__main__":
    app.run(debug=True, port=8000)