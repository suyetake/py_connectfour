import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

board = create_board()
game_over = False
num_players = 1
turn =0

print(board)
print()

#get number of players and exit if not valid
#python range must be set one+ larger than maximum int
num_players = int(input("Number of Players(1-4): "))
if num_players not in range(1,5):
    exit()

print()

#loop until game is over
#later:add game code, this will only get first turn of all players:

while not game_over and turn < num_players:
   #ask player/turn input
   turn = turn+1
   selection = int(input("Player "+str(turn)+" make your column selection(1-7): "))
   if selection not in range(1,8):
       exit(0)

#code not needed, handled in loop condition
#   if turn == int(num_players):
#       game_over = True


