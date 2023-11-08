from random import sample
from conectar import *  #Importando conexion BD



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
        
        cursor.execute("SELECT * FROM productos WHERE id = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarProducto(nombre='', descripcion='', marca='', precio='', stock='', imagen=''):       
        con = conexion()
        cursor           = con.cursor(dictionary=True)
            
        sql         = ("INSERT INTO productos(nombre,descripcion, marca,precio,stock,imagen) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        valores     = (nombre,descripcion, marca,precio,stock,imagen)
        cursor.execute(sql, valores)
        con.commit()
        cursor.close() #Cerrando conexion SQL
        con.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
        return resultado_insert
  

def detallesdelProductos(idProductos):
        con = conexion()
        cursor = con.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM productos WHERE id ='%s'" % (idProductos,))
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