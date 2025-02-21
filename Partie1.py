# définir le plateau de jeu
n=int(input("nombre d'allumettes"))
board = ["|" for i in range(n)]
print(board)

# L'ordinateur joue aléatoirement
import random


def play_random_move(board):
  a = random.randint(1, 3)
  return a, board[a:]

def play_random_move_V2(board):
  a = random.randint(1, 3)
  if len(board)-a>=3:
    return a, board[a:]
  elif len(board)==2:
    a = random.randint(1, 2)
  elif len(board)==1:
    return "Tu as perdu"
  else:
    return "Fin, tu as gagné"
  return a, board[a:]




a, newboard = play_random_move(board)
print(a, newboard)
a, newboard1 = play_random_move(newboard)
print(a, newboard1)


#Autre options: classe orientée objet
class Board:

  def __init__(self):
    self.board = ["|" for i in range(13)]

  def is_game_over(self):
    return len(self.board) == 0

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
