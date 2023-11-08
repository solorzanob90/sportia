from random import sample
from conectar import *  #Importando conexion BD
import os
from werkzeug.utils import secure_filename



#Creando una funcion para obtener la lista de Productoss.
def listaProductos():
    con = conexion() #creando mi instancia a la conexion de BD
    cur      = con.cursor(dictionary=True)

    querySQL = "SELECT * FROM productos"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    con.close() #cerrando conexion de la BD    
    return resultadoBusqueda




def updateProductos(id=''):
        con = conexion()
        cursor = con.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM productos WHERE id_producto = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarProducto(nombre='', descripcion='', marca='', precio='', stock='', imagen=''):       
        con = conexion()
        cursor           = con.cursor(dictionary=True)
            
        sql         = ("INSERT INTO productos(nombre,descripcion, marca,precio,stock,imagen) VALUES (%s, %s, %s, %s, %s, %s)")
        valores     = (nombre,descripcion, marca,precio,stock,imagen)
        cursor.execute(sql, valores)
        con.commit()
        cursor.close() #Cerrando conexion SQL
        con.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
        return resultado_insert
  

def detallesdelProducto(idProductos):
        con = conexion()
        cursor = con.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM productos WHERE id_producto ='%s'" % (idProductos,))
        resultadoQuery = cursor.fetchone()
        cursor.close() #cerrando conexion de la consulta sql
        con.close() #cerrando conexion de la BD
        
        return resultadoQuery
    
    

def  recibeActualizarProductos(nombre,descripcion, marca,precio,stock,imagen, idPro):
        con = conexion()
        cur = con.cursor(dictionary=True)
        cur.execute("""
            UPDATE Productoss
            SET 
                nombre   = %s,
                descripcion  = %s,
                marca    = %s,
                precio   = %s,
                stock = %s,
                imagen= %s,
            WHERE id=%s
            """, (nombre,descripcion, marca,precio,stock,imagen,  idPro))
        con.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        con.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update
 

#Crear un string aleatorio para renombrar la foto 
# y evitar que exista una foto con el mismo nombre
def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio

def recibeFoto(file):
    print(file)
    basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
    filename = secure_filename(file.filename) #Nombre original del archivo

    #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = stringAleatorio() + extension
    #print(nuevoNombreFile)
        
    upload_path = os.path.join (basepath, 'static/assets/img', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile



def eliminarProducto(idProd='', nombre_imagen=''):
        
    con = conexion() #Hago instancia a mi conexion desde la funcion
    cur  = con.cursor(dictionary=True)
    
    cur.execute('DELETE FROM productos WHERE id_producto=%s', (idProd,))
    con.commit()
    resultado_eliminar = cur.rowcount #retorna 1 o 0
    #print(resultado_eliminar)
    
    basepath = os.path.dirname (__file__) #C:\xampp\htdocs\localhost\Crud-con-FLASK-PYTHON-y-MySQL\app
    url_File = os.path.join (basepath, 'static/assets/fotos_carros', nombre_imagen)
    os.remove(url_File) #Borrar foto desde la carpeta
    #os.unlink(url_File) #Otra forma de borrar archivos en una carpeta
    

    return resultado_eliminar
