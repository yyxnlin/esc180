"""
ESC180 Assignment 2: Gomoku (Connect 5)
Lynn Tao
November 17, 2024

Starter code from Michael Guerzhoy with tests contributed by Siavash Kazemian.

To play against computer, uncomment last two lines (play_gomoku(8))
"""

def is_empty(board):
    for i in range (len(board)):
        for j in range (len(board[i])):
            if (board[i][j] != " "):
                return False
    return True
    
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    count = 0  

    if (0 <= x_end+d_x < len(board[0]) and 0 <= y_end+d_y < len(board)):
        if (board[y_end+d_y][x_end+d_x] != " "):
            count += 1
    else:
        count += 1
        

    if (0 <= x_end-length*d_x < len(board[0]) and 0 <= y_end-length*d_y < len(board)):
        if (board[y_end-length*d_y][x_end-length*d_x] != " "):
            count += 1
    else:
        count += 1

    if (count == 2):
        return ("CLOSED")
    elif (count == 0):
        return ("OPEN")
    else:
        return ("SEMIOPEN")

def in_range(board, y, x):
    if (0 <= x < len(board) and 0 <= y < len(board)):
        return True
    return False

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    pass
    open_seq_count = 0
    semi_open_seq_count = 0

    # x x x x x 
    for i in range (len(board) - length + 1): # loop through each first element
        sequence_found = True
        y_first_index = y_start + i*d_y
        x_first_index = x_start + i*d_x
        # len(board) - length + (length-1) = len(board)-1
        for j in range (length):
            if not in_range(board, y_first_index + j*d_y, x_first_index + j*d_x):
                sequence_found = False
                break
            if (board[y_first_index + j*d_y][x_first_index + j*d_x] != col):
                sequence_found = False
                break
        if (sequence_found):
            # check if it is complete sequence
            incomplete = False
            # 1. check before start
            if in_range(board, y_first_index - d_y, x_first_index - d_x):
                if board[y_first_index - d_y][x_first_index - d_x] == col:
                    incomplete = True

            # 2. check after end
            if in_range(board, y_first_index + (length)*d_y, x_first_index + (length)*d_x):
                if board[y_first_index + (length)*d_y][x_first_index + (length)*d_x] == col:
                    incomplete = True

            bounded = is_bounded(board, y_first_index + (length-1)*d_y, x_first_index + (length-1)*d_x, length, d_y, d_x)

            if (bounded == "OPEN" and not incomplete):
                open_seq_count += 1
            elif (bounded == "SEMIOPEN" and not incomplete):
                semi_open_seq_count += 1    
    return open_seq_count, semi_open_seq_count


def find_start(board, y, x, d_y, d_x):
    col = board[y][x]

    if (col == " "):
        return None, None
    i = 1

    while (0 <= x-i*d_x <= len(board) - 1 and 0 <= y-i*d_y <= len(board) - 1):
        # previous one in that direction is not equal
        if board[y-i*d_y][x-i*d_x] != col:
            # print ("x: ", x, "y: ", y, "diff1: ", x-i*d_x, "diff2: ", y-i*d_y)

            if (i > 1):
                return y-(i-1)*d_y, x-(i-1)*d_x

            # i is equal to 1
            else:
                break

        i += 1

    if (i > 1):
        return y-(i-1)*d_y, x-(i-1)*d_x

    # this one is the start
    elif (i == 1 and 0 <= x+d_x <= len(board) - 1 and 0 <= y+d_y <= len(board) - 1):
        if (board[y+d_y][x+d_x] == col):
            return y, x

    # this one is not the start
    return None, None

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    # check left and right sides
    for y_start in range (len(board)):
            for x_start in [0, len(board)-1]:
                for d_y, d_x in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                    add_open_count, add_semiopen_count = detect_row(board, col, y_start, x_start, length, d_y, d_x)
                    open_seq_count, semi_open_seq_count = open_seq_count + add_open_count, semi_open_seq_count + add_semiopen_count
    # check top and bottom
    for x_start in range (1, len(board)-1):
            for y_start in [0, len(board)-1]:
                for d_y, d_x in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                    add_open_count, add_semiopen_count = detect_row(board, col, y_start, x_start, length, d_y, d_x)
                    open_seq_count, semi_open_seq_count = open_seq_count + add_open_count, semi_open_seq_count + add_semiopen_count

    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    ret_y = 0
    ret_x = 0
    max_score = 0
    done = False

    for y in range (len(board)):
        if (done):
            break
        for x in range(len(board)):
            if (board[y][x] == " "):
                board[y][x] = "b"
                max_score = score(board)
                board[y][x] = " "
                done = True
                break

    for y in range (len(board)):
        for x in range(len(board)):
            if (board[y][x] == " "):
                board[y][x] = "b"
            else:
                continue

            if (score(board) > max_score):
                ret_y = y
                ret_x = x
                max_score = score(board)
            # print (y, x, ":", score(board))
            board[y][x] = " "
    return ret_y, ret_x


    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

    
def is_win(board):
    b_win = False
    w_win = False
    full = True
    found = False
    for y in range (len(board)):
        if(found):
            break
        for x in range (len(board)):
            if(found):
                break
            col = board[y][x]

            if (col == " "):
                full = False
                continue

            for d_y, d_x in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                for i in range (5):
                    if (in_range(board, y+i*d_y, x+i*d_x)):
                        

                        if (board[y+i*d_y][x+i*d_x] != col):
                            break
                        elif (i == 4):
                            found = True
                if (found):
                    if (col == "b"):
                        b_win  = True
                    elif (col == "w"):
                        w_win = True
    if (w_win):
        return "White won"
    elif (b_win):
        return "Black won"
    elif (full):
        return "Draw"
    else:
        return "Continue playing"


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    

    test_detect_rows()
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        # analysis(board)
        
        game_res = is_win(board)
        print(game_res)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res       
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
# if __name__ == '__main__':
#     play_gomoku(8)