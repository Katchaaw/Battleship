from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# Ajouter un "print (ship_row)" et un "print (ship_col)" pour connaître l'emplacement pour debug


# Loop
for turn in range(4):
  print("Tour", turn + 1)
  guess_row = int(input("Ligne: "))
  guess_col = int(input("Colonne: "))

  if guess_row == ship_row and guess_col == ship_col:
    print ("Félicitations! Tu a coulé mon sous-marin!")
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Ce n'est même pas dans l'océan...")
    elif board[guess_row][guess_col] == "X":
      print("Tu as déjà essayer cette endroit!")
    else:
      print ("Tu as loupé mon sous-marin!")
      board[guess_row][guess_col] = "X"
    print_board(board)
    if (turn == 3):
      print ("Game Over")
    
#Il faut régler le pb qui fait que lorsque l'on donne la valeur 5 à une coordonnées, on est considéré comme en dehors de l'océan
#Le pb vient du fait que l'on commence en 0 et pas en 1, pour l'afficher il faudrait faire comprendre à la machine que 0 = 0+1