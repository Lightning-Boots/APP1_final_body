# définir le plateau de jeu



# L'ordinateur joue aléatoirement
import random


def play_random_move(board):
  a = random.randint(1, 3)
  return a, board[a:]

def play_random_move_V2(board):
  a = random.randint(1, 3)
  if len(board)-a>=0:
    return a, board[a:]
  elif len(board)==2:
    a = random.randint(1, 2)
  elif len(board)==1:
    a=1
  else:
    return board
  
  return a, board[a:]



board = ["|" for i in range(4)]
print(board)
a, newboard = play_random_move_V2(board)
print(a, newboard)
a, newboard1 = play_random_move_V2(newboard)
print(a, newboard1)