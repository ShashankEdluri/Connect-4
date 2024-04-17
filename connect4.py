# Name : Shashank Edluri 
# Email : sedluri@umass.edu
# Spire ID : 34428126

def make_empty_board(nrows, ncol):
    board = []
    board.append('.' * ncol)
    answer = board * nrows
    return (answer)        

# print (make_empty_board(6,2))

def print_board(inp):
    index = {'X' : ' x ', 'O': ' o ', '.': ' . '}

    for i in range(len(inp)):
        yyy = inp[i]
        print ('|'.join(index[char] for char in yyy))
        if i != len(inp)-1:
            print ('---+' * len(yyy))

# print_board([".......", ".......", "..O....", "..OX...", ".O.OX..",".OXXOXX"])

def verify_board(inp):
    rows = len(inp)
    countx = 0 
    counto = 0 
    for x in inp:
        for y in x:    
            if y == 'X':
                countx += 1
            elif y == 'O':
                counto += 1
    if abs(countx - counto) >= 2:
        return False
    for row_index in range(rows-1): 
        for column_index in range(len(inp[0])):
            d = inp[row_index][column_index].upper()
            n = inp[row_index+1][column_index].upper()
            if d != '.' and n == '.':
                return False
            else:
                return True

def verify_move(board, column):
    columns = len(board[0])
    rows = len(board)
    if column < 0 or column >= columns:
        return False
    if board[0][column] == '.':
        return True
    return False

board = ["..O....", "..X....", "..O....", "..OX...", ".OXOX..",".OXXOX."] 
print(verify_move(board, 1))

def update_board():
    






