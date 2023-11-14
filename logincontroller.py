from flask import Flask, request, jsonify,redirect,url_for,session
import mysql.connector
from conectar import *
from crud_controller import *

app = Flask(__name__)   

db = conexion()

def loguear(username,password):
    try:
       
        # Crea un cursor
        cursor = db.cursor()

        # Ejecuta la consulta para obtener el usuario
        cursor.execute("SELECT * FROM admins WHERE user = %s", (username,))

        # Obtiene el resultado
        usuario = cursor.fetchone()

        if (usuario is not None and usuario[2] == password and usuario[1] == username ):
            # El usuario y la contraseña son correctos
            print('El usuario y la contraseña son correctos')
            #return jsonify({'mensaje': 'Inicio de sesión exitoso'})
            return True
        else:
            # El usuario o la contraseña son incorrectos
            #return jsonify({'mensaje': 'Usuario o contraseña incorrectos'})
            return False
            print('El usuario y la contraseña son incorrectos')
    except Exception as e:
        return jsonify({'error': str(e)})
        print(str(e))
    finally:
        # Cierra el cursor después de usarlo
        cursor.close()

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main':
    app.run(debug=True)
