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