import random

def play_random_move_V2(nombre_allumette, Coup_max):
  if Coup_max < nombre_allumette :
    a = random.randint(1,Coup_max)
  else :
    a = random.randint(1,nombre_allumette)
  return a


