# Tic Tac Toe game with Python 

board = [' ' for i in range(10)] 

def insertLetter(letter, pos):
    board[pos] = letter

def printBoard():
    print('   ||   ||')
    print(' ' + board[1] + ' || ' + board[2] + ' || ' + board[3])
    print('   ||   ||')
    print('===++===++===')
    print('   ||   ||')
    print(' ' + board[4] + ' || ' + board[5] + ' || ' + board[6])
    print('   ||   ||')
    print('===++===++====')
    print('   ||   ||')
    print(' ' + board[7] + ' || ' + board[8] + ' || ' + board[9])
    print('   ||   ||')

def isWinner(board_pos, letter):
    return( board[1] == letter and board[2] == letter and board[3] == letter or
        board[4] == letter and board[5] == letter and board[6] == letter or
        board[7] == letter and board[8] == letter and board[9] == letter or
        board[1] == letter and board[4] == letter and board[7] == letter or
        board[2] == letter and board[5] == letter and board[8] == letter or
        board[3] == letter and board[6] == letter and board[9] == letter or
        board[1] == letter and board[5] == letter and board[9] == letter or
        board[3] == letter and board[5] == letter and board[7] == letter )

def spaceisFree(pos):
    return board[pos] == ' '

def playerMove():
    
    flag = True

    while flag:
        letter = input(' Enter Position to insert your \'X\' : ') 
        try:
            letter = int(letter)
            if 0 > letter > 9:
                print('Please enter a valid position !!!')
            if spaceisFree(letter):
                insertLetter('X', letter)
        except:
            pass
        break

def isBoardfull(board):
    if board.count(' ') > 1:
        return True
    else:
        return False

def main():
    print('\n<====  Welcome to the Tic Tac Toe  ====>\n')
    printBoard()

    while not(isBoardfull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
            break
        else:
            print("Sorry, \'O\' wins the game !")
            break

        if not(isWinner(board, 'X')):
            playerMove()
            printBoard()
        else:
            print("Sorry, \'X\' wins the game !")
            break

    if isBoardfull(board):
        print(' Game Tied !!!! ')

main()