from flask import render_template, request 
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/play')
def play():
    player_name = request.form['name']
    player_choice = request.form['choice']
    player = player (player_name, player_choice)
    new_game = Game ()
    new_game.play (player)
    print (request.form)
    return render_template ('index.html')

