from random import randint
'''
Board Layout:

1|2|3
-----
4|5|6
-----
7|8|9

'''

board = [[' ','|',' ','|',' '],
        ['-','-','-','-','-'],
        [' ','|',' ','|',' '],
        ['-','-','-','-','-'],
        [' ','|',' ','|',' ']]

def showBoard():
    for i in board:
        print("".join(i))

def evaluate():

    point = int(input('Please input your tile (1 is top left, 9 is bottom right): '))

    # Complete the evaluate function, so that the function checks if the input is valid (between 1 and 9) and the tile is free. Also if the tile is free sets 'X' on the tile. In case the tile is not free the function should return False
    # and print 'There is already a tile at your given position!'
    # Code start (18 Lines of code)
    
    # Code end
    return True

def checkWin():
    # Check rows
    if board[0][0] == board[0][2] == board[0][4] == 'X':
        print('You win!')
        return True
    if board[0][0] == board[0][2] == board[0][4] == 'O':
        print('You lose!')
        return True
    if board[2][0] == board[2][2] == board[2][4] == 'X':
        print('You win!')
        return True
    if board[2][0] == board[2][2] == board[2][4] == 'O':
        print('You lose!')
        return True
    if board[4][0] == board[4][2] == board[4][4] == 'X':
        print('You win!')
        return True
    if board[4][0] == board[4][2] == board[4][4] == 'O':
        print('You lose!')
        return True
    # Check columns
    if board[0][0] == board[2][0] == board[4][0] == 'X':
        print('You win!')
        return True
    if board[0][0] == board[2][0] == board[4][0] == 'O':
        print('You lose!')
        return True
    if board[0][2] == board[2][2] == board[4][2] == 'X':
        print('You win!')
        return True
    if board[0][2] == board[2][2] == board[4][2] == 'O':
        print('You lose!')
        return True
    if board[0][4] == board[2][4] == board[4][4] == 'X':
        print('You win!')
        return True
    if board[0][4] == board[2][4] == board[4][4] == 'O':
        print('You lose!')
        return True
    # Check diagonals
    if board[0][0] == board[2][2] == board[4][4] == 'X':
        print('You win!')
        return True
    if board[0][0] == board[2][2] == board[4][4] == 'O':
        print('You lose!')
        return True
    if board[4][0] == board[2][2] == board[0][4] == 'X':
        print('You win!')
        return True
    if board[4][0] == board[2][2] == board[0][4] == 'O':
        print('You lose!')
        return True
    # Check if board is full
    full = True
    for i in range(5):
        for j in range(5):
            if board[i][j] == ' ':
                full = False
    if full == True:
        print("Draw!")
        return True
    return False

def kiMove():
    set = False
    while not set:
        a = randint(0,4)
        b = randint(0,4)
        if board[a][b] == ' ':
            board[a][b] = 'O'
            set = True

if __name__ == '__main__':
    while True:
        showBoard()
        while True:
            check = evaluate()
            if check: break
        win = checkWin()
        if win: break
        kiMove()
        checkWin()