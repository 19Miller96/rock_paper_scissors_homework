class Player():

    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

class Game():

    def decide_a_winner(Player_1, Player_2):
        if Player_1.choice() == Player_2.choice():
            return 'Draw!'
        elif Player_1.choice() == 'Rock' and Player_2.choice() == 'Paper':
            return 'Player 2 won!'
        elif Player_1.choice() == 'Rock' and Player_2.choice() == 'Scissors':
            return 'Player 1 won!'
        elif Player_1.choice() == 'Scissors' and Player_2.choice() == 'Paper':
            return 'Player 1 won!'
        elif Player_1.choice() == 'Scissors' and Player_2.choice() == 'Rock':
            return 'Player 2 won!'
