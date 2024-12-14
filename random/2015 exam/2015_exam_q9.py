
#1 mark for look-ahead by 1 move
#2 for "don't know" or blank


import copy


# FROM SANTA.PY:
def is_row_all_three(board, mark, row_num):
    return board[row_num] == [mark] * 3
    
def is_col_all_three(board, mark, col_num):
    for i in range(3):
        if board[i][col_num] != mark:
            return False
    return True
    
def is_left_diag_all_three(board, mark):
    for i in range(3):
        if board[i][i] != mark:
            return False
    return True
    
def is_right_diag_all_three(board, mark):
    for i in range(3):
        if board[i][2-i] != mark:
            return False
    return True

def is_win(board, mark):
    for i in range(3):
        if is_row_all_three(board, mark, i):
            return True
    
    for i in range(3):
        if is_col_all_three(board, mark, i):
            return True
            
    if is_right_diag_all_three(board, mark):
        return True
        
    if is_left_diag_all_three(board, mark):
        return True
        
    return False

    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
    

def x_won(board):
    return is_win(board, "X")



# MY SOLUTION:
def get_empty_cells(board):
    res = []

    for i in range(len(board)):
        for j in range (len(board)):
            if board[i][j] == " ":
                res.append([i, j])

    return res

def x_will_win(board):
    if x_won(board):
        return True
    
    empty_cells = get_empty_cells(board)

    if len(empty_cells) == 0:
        return False
    
    
    for e in empty_cells:
        board[e[0]][e[1]] = "X"

        could_win = True

        for e2 in empty_cells:
            if e != e2:
                board[e2[0]][e2[1]] = "O"
                if not x_will_win(board):
                    could_win = False
                    break

                board[e2[0]][e2[1]] = " "

        board[e[0]][e[1]] = " "

        if could_win and len(empty_cells) > 2:
            return True
        
    return False


print(x_will_win([[" ", "X", " "], 
                  [" ", "X", " "],
                  [" ", "O","O"]]))


print(x_will_win([[" ", " ", " "], 
                  [" ", "X", "O"],
                  [" ", " ", " "]]))

print(x_will_win([[" ", " ", " "], 
                  [" ", " ", " "],
                  [" ", " ", " "]]))    




