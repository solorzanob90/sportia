from flask import Flask, render_template, request, redirect, url_for, session
from conectar import *

app = Flask(__name__)   

def verificaradmin(username, password):

        # Consulta para verificar las credenciales del usuario
       
        if username=='admin' and password=='1234':
          print("accedió el admin")

          return True
          # return redirect(url_for('home'))
        
        else:
            return False

      
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main':
    app.run(debug=True)

