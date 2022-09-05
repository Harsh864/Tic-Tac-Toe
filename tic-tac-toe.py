import time

def welcome():
    print("Welcome to the Tic-Tac-Toe Game\n")
    name = input("Enter your name ")
    print("Welcome to this game \n"+ name)
    print("Let's begin the Game...\nOn the count of \n3...")
    time.sleep(2)
    print("2...")
    time.sleep(2)
    print("1...\n")
    time.sleep(1)

theBoard = {'7':' ', '8':' ', '9':' ',
            '4':' ', '5':' ', '6':' ',
            '1':' ', '2':' ', '3':' '}

theKey = []
for keys in theBoard:
    theKey.append(keys)

def printBoard(board):
    print(board['7'] + "|" + board['8'] + "|" + board['9'] + "\n")
    print("--+--")
    print(board['4'] + "|" + board['5'] + "|" + board['6'] + "\n")
    print("--+--")
    print(board['1'] + "|" + board['2'] + "|" + board['3'] + "\n")

def game():
    turn = 'X'
    count = 0

    welcome()

    for _ in range(10):
        printBoard(theBoard)
        print("Your turn " + turn)
        user = input()
        

        if theBoard[user] == ' ':
            theBoard[user] = turn
            count+=1
        else:
            print("Sorry!!! this place is already filled\n")
            continue

        if count >= 5:

            if (theBoard['7'] == theBoard['8'] == theBoard['9']!=' ' or 
                theBoard['4'] == theBoard['5'] == theBoard['6']!=' ' or
                theBoard['1'] == theBoard['2'] == theBoard['3']!=' ' or
                theBoard['7'] == theBoard['4'] == theBoard['1']!=' ' or
                theBoard['8'] == theBoard['5'] == theBoard['2']!=' ' or
                theBoard['9'] == theBoard['6'] == theBoard['3']!=' ' or 
                theBoard['7'] == theBoard['5'] == theBoard['3']!=' ' or 
                theBoard['1'] == theBoard['5'] == theBoard['9']!=' '):
                printBoard(theBoard)
                print("MR. " + turn + " has WON!!! the Game\n")
                break
        
        if count == 9:
            print("Game Over!!!")
            print("It's Tie")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    print("You want to reset the game: (y/n)")
    play = input()
    if play == 'y' or play == 'Y':
        for key in theKey:
            theBoard[key] = ' '
        game()

if __name__ == '__main__':
    game()