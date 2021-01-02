theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []
for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7']+ '|'+ board['8']+ '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        print("Your turn "+ turn+".Move to which place?")
        move = input()
        if theBoard[move]==' ':
            theBoard[move]= turn
            count = count + 1
        else:
            print('That place is already filled. \n Move to another spot.')
            continue
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\n Game Over. \n')
                print(turn + ' won')
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print('\n Game Over. \n')
                print(turn + ' won')
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\n Game Over. \n')
                print(turn + ' won')
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\n Game Over. \n')
                print(turn + ' won')
                break
            elif theBoard['9'] == theBoard['5'] == theBoard['1'] != ' ':
                printBoard(theBoard)
                print('\n Game Over. \n')
                print(turn + ' won')
                break
            elif theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
                printBoard(theBoard)
                print('\n Game Over. \n')
                print(turn + ' won')
                break
            elif theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ':
                printBoard(theBoard)
                print('\n Game Over. \n')
                print(turn + ' won')
                break
            elif theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\n Game Over. \n')
                print(turn + ' won')
                break
        if count ==9:
            print("\n Game Over.\n ")
            print('TIE')
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart =  input('Do you want to play again?\n')
    if restart == 'yes' or restart == 'Yes' or restart == 'YES':
        for key in board_keys:
            theBoard[key]= ' '
        game()
if __name__ == "__main__":
    game()