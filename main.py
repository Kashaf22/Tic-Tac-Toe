
def printBoard(xState, zState):
   zero = 'X' if xState[0] else ('O' if zState[0] else 0)
   one = 'X' if xState[1] else ('O' if zState[1] else 1)
   two ='X' if xState[2] else ('O' if zState[2] else 2)
   three = 'X' if xState[3] else ('O' if zState[3] else 3)
   four = 'X' if xState[4] else ('O' if zState[4] else 4)
   five = 'X' if xState[5] else ('O' if zState[5] else 5)
   six = 'X' if xState[6] else ('O' if zState[6] else 6)
   seven = 'X' if xState[7] else ('O' if zState[7] else 7)
   eight = 'X' if xState[8] else ('O' if zState[8] else 8)
   print(f"{zero} | {one} | {two} ")
   print(f"--|---| --")
   print(f"{three} | {four} | {five} ")
   print(f"--|---| --")
   print(f"{six} | {seven} | {eight} ")

#Over-writing the sum function because in python it only takes 2 arguments and we want 3  
def sum(a, b, c ):
    return a + b + c

   
def checkWin(xState, zState):
    #wins 2D array has all the possibilities in which a user can win
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        # if statements checking if each one of the array in the 2D array 
        # indices in the Xstate or Ostate add up to 3 
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 0
    #we return -1 if none of them won. This is a tie situation.
    return -1


if __name__ == "__main__":
   # we declared a list with 8 zeros because our game board will have 
   # 8 zeros
   xState = [0,0,0,0,0,0,0,0,0]
   zState = [0,0,0,0,0,0,0,0,0]
   # The value of turn is 1 for X and 0 for O
   turn = 1 
   print("Welcome to Tic Tac Toe")
   while(True):
    printBoard(xState, zState)
    if(turn == 1):
        print("X's turn")
        value = int(input("Please enter a value: "))
        xState[value] = 1
    else: 
        print("O's turn")
        value = int(input("Please enter a value: "))
        zState[value] = 1
    # checking if any of them won before moving to a next turn 
    cwin = checkWin(xState, zState)
    if(cwin != -1):
            print("Match over")
            break
        
    turn = 1 - turn