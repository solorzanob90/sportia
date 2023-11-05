import mysql.connector

#conexion = mysql.connector.connect(user='root', password='',host='localhost', database='mysportia', port='3306' )

def conexion():
    mydb=mysql.connector.connect(user='root', password='',host='localhost', database='sport', port='3306' )
    if mydb:
        print("Conexion Exitosa")
        return mydb
    else:
        print("Error de Conexion")