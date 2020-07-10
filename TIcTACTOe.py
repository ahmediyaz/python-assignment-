
board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
b_keys = []
for i in board:
    b_keys.append(i)
def printTheBoard(board1):
    print(board1['7'] + '|' + board1['8'] + '|' + board1['9'])
    print('-+-+-')
    print(board1['4'] + '|' + board1['5'] + '|' + board1['6'])
    print('-+-+-')
    print(board1['1'] + '|' + board1['2'] + '|' + board1['3'])
def gametictactoe():
    turn = 'X'
    c = 0
    for i in range(10):
        printTheBoard(board)
        print("It's your turn," + turn + ".Move to which place?")
        m = input()        
        if theBoard[m] == ' ':
            board[m] = turn
            c += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue 
        if c >= 5:
            if board['7'] == board['8'] == board['9'] != ' ': 
                printTheBoard(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif board['4'] == board['5'] == board['6'] != ' ': 
                printTheBoard(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                printTheBoard(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                printTheBoard(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board['3'] == board['6'] == board['9'] != ' ': 
                printTheBoard(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif board['7'] == board['5'] == board['3'] != ' ':
                printTheBoard(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board['1'] == board['5'] == board['9'] != ' ': 
                printTheBoard(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for k in b_keys:
            board[k] = " "

        gametictactoe()

if __name__ == "__main__":
    gametictactoe()
