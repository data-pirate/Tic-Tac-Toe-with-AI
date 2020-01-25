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

def main():
    printBoard(board)

main()