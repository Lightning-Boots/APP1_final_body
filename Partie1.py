# définir le plateau de jeu
board = ["|" for i in range(13)]
print(board)

# L'ordinateur joue aléatoirement
import random


def play_random_move(board):
  a = random.randint(1, 3)
  return a, board[a:]


a, newboard = play_random_move(board)
print(a, newboard)
a, newboard1 = play_random_move(newboard)
print(a, newboard1)


#Autre options: classe orientée objet
class Board:

  def __init__(self):
    self.board = ["|" for i in range(13)]

  def play_random_move(self):
    if is_game_over(self)==False:
        a = random.randint(1, 3)
        return a, self.board[a:]
    else:
      return "Game Over"

  # en plus
  def play_human_move(self, move):
    return self.board[move:]

  def is_game_over(self):
    return len(self.board) == 0
