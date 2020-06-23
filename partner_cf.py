# Partner's Connect Four program in Python
# partner_cf.py

import numpy as np
ROW_COUNT=6
COL_COUNT=7

def create_board():
  board = np.zeros((ROW_COUNT,COL_COUNT))
  return board

def is_valid_location(board, col):
  return board[ROW_COUNT-1][col]==0

def get_next_open_row(board, col):
  for r in range(ROW_COUNT):
    if board [r,col]==0:
      return r

#check 4 directions to see if game is won in this move
def won_game(board, col, row, turn):

  #check down
  match=1
  for r in range(max(row-4,0),row):
    if board[r,col]==turn:
      match+=1
    else:
        match=1
  if match==4:
    return turn

  #check side to side
  match=1
  for c in range(max(col-3,0),min(col+3, COL_COUNT-1)):
    if board[row,c]==turn:
      match+=1
      if match==4:
        return turn
    else:
      match=1

  #check diag right and up
  match=0
  for i in range(-3,3):
   #if it's on the board
   if i+row in range(ROW_COUNT) and i+col in range(COL_COUNT):
     if board[row+i,col+i]==turn:
       match+=1
     else:
       match=0
     if match==4:
       return turn
  #check diag right and down
  match=0
  for i in range(-3,3):
   #if it's on the board
   if row-i in range(ROW_COUNT) and i+col in range(COL_COUNT):
     if board[row-i,col+i]==turn:
       match+=1
     else:
       match=0
     if match==4:
       return turn
  #return number for player that won or zero if no wins yet..
  return 0

def drop_piece (board,row,col,turn):
  board[row][col]=turn

def print_board(board):
  print(np.flip(board,0)) #over x axis that's what the zero means

board=create_board()
play_game_still = True
turn = 1
while play_game_still:
  col = int (input("Player "+str(turn)+" make your selection (0-6)"))
  if is_valid_location(board,col):
   row=get_next_open_row(board,col)
   drop_piece(board,row,col,turn)
   print_board(board)
   if won_game(board, col, row, turn)==turn:
     print("Congrats player number "+str(turn))
     exit()
  #change who's turn it is
  turn=turn %2
  turn=turn+1



