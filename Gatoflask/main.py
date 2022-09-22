'''
Template basado en https://github.com/rfinz/flasktactoe

para evitar usar numpy, se puede usar >from random import randint
'''

from flask import Flask, render_template, request, redirect, url_for
# imports de lógica



app = Flask(__name__)

# Creacion de bots


'''
Nota: el @ se usa para añadir un decorador a una función.
''' 
@app.route("/setup", methods=['GET'])
def setup():
    return render_template('setup.html');

@app.route("/setup", methods=['POST'])
def update_setup():
    # Creación del tablero


    return redirect(url_for('index'))

@app.route("/restart")
def restart():
    # Creación del tablero
 
 
    return redirect(url_for('index'))

@app.route("/", methods=['GET'])
def index():
    # condicion: board no ha sido inicializado
        return redirect(url_for('setup'))

    # condicion: si el jugador juega de segundo y es el primer movimiento
        # entonces, aplicar movimiento del bot


    return render_template('index.html', 
                           grid = board.board,
                           win = board.winner)

@app.route("/", methods=['POST'])
def update():
    global board
    if board.winner is None:

        # obtención de fila y columna usando request.form['play']
        

        # aplicar movimiento
        

        # aplicar movimiento del bot, añadiendo una condicion para que el
        # primer movimiento sea aleatorio
        
    

    return render_template('index.html', 
                           grid = board.board,
                           win = board.winner)

if __name__ == "__main__":
    app.run(debug=True)
