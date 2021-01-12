import os
import time
import random

board = [" "," "," "," "," "," "," "," "," "," ",]

def print_title():

    print("""         (っ◔◡◔)っ ♥ tic tac toe ♥
                                    key:

                                    1|2|3
                                    -----
                                    4|5|6
                                    -----
                                    7|8|9

        Instructions: Wtf you don't know how to... I- ummm you gotta get the
        three thingys in a row, you chose your place corresponding to the key
        above. Good luck : ) ps u need a friend to play with you 


          """


          )

def do_board():

    print("___|___|___")    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("   |   |   ") 

while True:
    os.system ("clear")
    print_title()
    do_board()


    choice = input("Pick an empty space for your move (X)!")
    choice = int(choice)

    if board[choice] == " ":
        board[choice] = "X"

    else:
            print ("oops thats not empty!")
            time.sleep(1)

    if (board[1] == "X" and board[2] == "X" and board[3] == "X") or \
       (board[4] == "X" and board[5] == "X" and board[6] == "X") or \
       (board[7] == "X" and board[8] == "X" and board[9] == "X") or \
       (board[1] == "X" and board[4] == "X" and board[8] == "X") or \
       (board[2] == "X" and board[5] == "X" and board[8] == "X") or \
       (board[3] == "X" and board[6] == "X" and board[9] == "X") or \
       (board[1] == "X" and board[5] == "X" and board[9] == "X") or\
       (board[3] == "X" and board[5] == "X" and board[7] == "X") :
        os.system("clear")
        print_title()
        do_board

        print("Daaamn you r smart you win!: )")
        break

    os.system ("clear")
    print_title()
    do_board()

    
    choice = input("Pick an empty space for your move(O)!")
    choice = int(choice)
    
    

    if board[choice] == " ":
        board[choice] = "O"

    else:
            print ("oops thats not empty!")
            time.sleep(1)

    if (board[1] == "O" and board[2] == "O" and board[3] == "O") or \
       (board[4] == "O" and board[5] == "O" and board[6] == "O") or \
       (board[7] == "O" and board[8] == "O" and board[9] == "O") or \
       (board[1] == "O" and board[4] == "O" and board[8] == "O") or \
       (board[2] == "O" and board[5] == "O" and board[8] == "O") or \
       (board[3] == "O" and board[6] == "O" and board[9] == "O") or \
       (board[1] == "O" and board[5] == "O" and board[9] == "O") or\
       (board[3] == "O" and board[5] == "O" and board[7] == "O") :
        os.system("clear")
        print_title()
        do_board

        print("Daaamn you r smart you win!: )")
        break

    tie = True
    for index in range (1, 10):
        if board[index] == " ":
            tie = False
            break

    if tie == True:
        print ("Wow that's a tie")
        break
        
    
    
    


