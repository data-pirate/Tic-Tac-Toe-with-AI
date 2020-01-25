# Tic Tac Toe game with Python 

board = [' ' for i in range(10)] 

def insertLetter(letter, pos):
    board[pos] = letter

def printBoard(board):
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

def isBoardfull(board):
    pass

def main():
    print('\n<====  Welcome to the Tic Tac Toe  ====>\n')
    printBoard(board)

    while not(isBoardfull(board)):
        break

    if isBoardfull(board):
        print(' Game Tied !!!! ')

main()