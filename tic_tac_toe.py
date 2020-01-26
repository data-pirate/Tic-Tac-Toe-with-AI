# Tic Tac Toe game with Python 
import random

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

def isWinner(board, letter):
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
            if 0 < letter < 10:
                if spaceisFree(letter):
                    flag = False
                    insertLetter('X', letter)
                else:
                    print('That space is occupied !!')
            else:
                print('Please enter a valid position !!!')

        except:
            print(' Type a number You enterd:',letter)

def isBoardfull(board):
    return board.count(' ') < 1

def selectRandom(lst):
    
    return lst[random.randrange(1,len(lst))]


def compMove():
    move = 0

# collecting all the possible moves

    available_places = [i for i, letter in enumerate(board) if letter == ' ' and i != 0]
    
    for each in ['X', 'O']:
        for i in available_places:
            cpy = list(board)
            cpy[i] = each #Checking if the player will win using next move , The computer will try to block that move
            if isWinner(cpy, each):
                move = i
                return move

# checking if the corners positions are available 

    corners = list()
    for i in available_places:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners) > 0:
        move = selectRandom(corners)
        return move

# checking if the center is available

    if 5 in available_places:
        move = 5
        return move

# check if position 2, 4, 6 ,8 are available

    center_pos = list()
    for i in available_places:
        if i in [2,4,6,8]:
            center_pos.append(i)
    if len(center_pos) > 0:
        move = selectRandom(center_pos)
        
    return move

    

def main():
    print('\n<====  Welcome to the Tic Tac Toe  ====>\n')
    printBoard(board)

    while not(isBoardfull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, \'O\' wins the game !")
            break

        if not(isWinner(board, 'X')):
            
            move = compMove()
            if move == 0:
                print('Game Tied !!!!!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' at position {}'.format(move))
                printBoard(board)
        else:
            print("Hurray !, \'X\' wins the game !")
            break

    if isBoardfull(board):
        print(' Game Tied !!!! ')

main()