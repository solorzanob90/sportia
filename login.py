from flask import Flask, render_template, request, redirect, url_for, session
from conectar import *
from crud_controller import *

app = Flask(__name__)   

def verificaradmin(username, password):
<<<<<<< HEAD
# Consulta para verificar las credenciales del usuario
  if (username=='admin' and password=='1234'):
    print("accedió el admin")
    resultados = listaProductos()
    return resultados
   
=======

        # Consulta para verificar las credenciales del usuario
        
        if username=='admin' and password=='1234':
          print("accedió el admin")
          resultados = listaProductos()
          return resultados
          # return redirect(url_for('home'))
        
       
>>>>>>> fcda45b956c1b15689ec9ea7f830b09366dffff1

      
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main':
    app.run(debug=True)

