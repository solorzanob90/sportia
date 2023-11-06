
from conectar import *
import random

def showProductInPage():
    #imagen,precio,nombre,marca
    cc=conexion()
    cur = cc.cursor(dictionary=True)

    query = "select * from productos"
    cur.execute(query)

    resultado = cur.fetchall()
    totalresultado =len(resultado)

    cur.close()
    cc.close()

    return resultado


def detalleprod(prod_id=''):
    cc=conexion()
    query=cc.cursor(dictionary=True)
    query.execute("SELECT * FROM productos WHERE id_producto = %s" % (prod_id))
    resultado = query.fetchone()
    query.close()
    cc.close()
    return resultado


#para el id del producto, 
#se usaran numero aleatorio
#sin repetirse
minimo=1
maximo=999 #ULTRA IMPORTANTE DEJAR ESTO ASI CON ESTE VALOR, SI PONES 9999 o mas, deja de funcionar
numeros = list(range(minimo,maximo+1))
random.shuffle(numeros)
id_pedido = numeros.pop()



def registrarUsuario(cedula=0,nombre='',apellido='',telefono='',direccion='',email='',total=0.0,idprod=0,cantidad=0,stockactual=0):
    cc=conexion()
    query=cc.cursor(dictionary=True)
    clienteRegPrv = ("SELECT * FROM cliente WHERE cedula=%s" % (cedula)) #cliente ya registrado con anterioridad
    sql = ("INSERT INTO cliente(cedula,nombre,apellido,telefono,direccion,email) VALUES (%s, %s, %s, %s, %s, %s)")
    venta = ("INSERT INTO ventas (id_pedido, cedula, total, estado) VALUES (%s, %s, %s, %s)")
    valoressql = (cedula,nombre,apellido,telefono,direccion,email)
    valoresventa = (id_pedido,cedula,total,"pagado")

    query.execute(clienteRegPrv)
    clReg = query.fetchone()
    if(clReg):#verifico si el cliente esta registrado primero
        #hago la venta con la cedula existente
        query.execute(venta,valoresventa) #registra la venta
        query.execute("INSERT INTO `detalleventas`(`id_pedido`, `id_producto`, `cantidad`) VALUES (%s,%s,%s)",(id_pedido,idprod,cantidad))#registra un detalle de venta
        query.execute("UPDATE `productos` SET `stock`=%s WHERE id_producto=%s" % (stockactual,idprod))
        cc.commit()
        query.close()
        cc.close()
        resultado = query.rowcount
        return resultado
    else:
        query.execute(sql,valoressql)
        query.execute(venta,valoresventa) #registra la venta
        query.execute("INSERT INTO `detalleventas`(`id_pedido`, `id_producto`, `cantidad`) VALUES (%s,%s,%s)",(id_pedido,idprod,cantidad))#registra un detalle de venta
        query.execute("UPDATE `productos` SET `stock`=%s WHERE id_producto=%s" % (stockactual,idprod))
        cc.commit()
        query.close()
        cc.close()
        resultado = query.rowcount
        return resultado