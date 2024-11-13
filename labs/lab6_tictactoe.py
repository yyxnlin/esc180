# ESC180 Lab 6 (Part 2)
# October 16, 2024

'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
    
def find_coord(square_num):
    coord = [(int)((square_num-1)/3), (int)((square_num-1)%3)]
    return coord

def put_in_board(board, mark, square_num):
    coord = find_coord(square_num)
    board[coord[0]][coord[1]] = mark

def get_free_squares(board):
    coord = []
    for i in range (3):
        for j in range (3):
            if (board[i][j] == " "):
                coord.append([i, j])
    return coord



def get_input(board, player):
    x_input = (int)(input("Enter coordinate for " + player + ": "))

    while (x_input <= 0 or x_input > 9 or board[find_coord(x_input)[0]][find_coord(x_input)[1]] != " "):
        x_input = (int)(input("Invalid!!! Enter coordinate for " + player + ": "))

    return x_input

def make_random_move(board, mark):
    i = (int(3 * random.random()))
    j = (int(3 * random.random()))

    while (board[i][j] != " "):
        i = (int(3 * random.random()))
        j = (int(3 * random.random()))

    board[i][j] = mark


def is_row_all_marks(board, row_i, mark):
    if (board[row_i][0] == mark and board[row_i][1] == mark and board[row_i][2] == mark):
        return True
    return False


def is_col_all_marks(board, col_i, mark):
    if (board[0][col_i] == mark and board[1][col_i] == mark and board[2][col_i] == mark):
        return True
    return False

def is_win(board, mark):
    for i in range (3):
        if (is_col_all_marks(board, i, mark) or is_row_all_marks(board, i, mark)):
            return True
    return False


if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    
    # print (find_coord(7))
    
    # print_board_and_legend(board)     

    # put_in_board(board, "O", 4)    
    # print_board_and_legend(board)  
    # print(get_free_squares(board))
    # make_random_move(board, "X")
    # print_board_and_legend(board)  




    # player vs player
    # filled_spots = 0

    # while (filled_spots != 9):   
        
    #     x_input = get_input(board, "X")
    #     put_in_board(board, "X", x_input)
    #     print_board_and_legend(board)  
    #     filled_spots+=1

    #     if (filled_spots != 9):
    #         o_input = get_input(board, "O")
    #         put_in_board(board, "O", o_input)
    #         print_board_and_legend(board)  
    #         filled_spots+=1



        
    # computer vs player
    filled_spots = 0
    game_over = False

    while (filled_spots != 9 and not game_over):   

        x_input = get_input(board, "X")
        put_in_board(board, "X", x_input)
        print_board_and_legend(board)  
        filled_spots+=1
        if is_win(board, "X"):
            print("Player wins!")
            game_over = True
        

        if (not game_over and filled_spots != 9):
            # no smart
            # make_random_move(board, "O")


            # smart
            placed = False

            for i in range (3):
                if (board[i][0] == board[i][1] == "O" and board[i][2] == " "):
                    put_in_board(board, "O", i*3+3)
                    placed = True
                    break
                elif (board[i][0] == board[i][2] == "O" and board[i][1] == " "):
                    put_in_board(board, "O", i*3+2)
                    placed = True
                    break
                elif (board[i][1] == board[i][2] == "O" and board[i][0] == " "):
                    put_in_board(board, "O", i*3+1)
                    placed = True
                    break
                elif (board[0][i] == board[1][i] == "O" and board[2][i] == " "):
                    put_in_board(board, "O", 6+i+1)
                    placed = True
                    break
                elif (board[0][i] == board[2][i] == "O" and board[1][i] == " "):
                    put_in_board(board, "O", 3+i+1)
                    placed = True
                    break
                elif (board[1][i] == board[2][i] == "O" and board[0][i] == " "):
                    put_in_board(board, "O", i+1)
                    placed = True
                    break
            
            if (not placed):
                for i in range (3):
                    if (board[i][0] == board[i][1] == "X" and board[i][2] == " "):
                        put_in_board(board, "O", i*3+3)
                        break
                    elif (board[i][0] == board[i][2] == "X" and board[i][1] == " "):
                        put_in_board(board, "O", i*3+2)
                        break
                    elif (board[i][1] == board[i][2] == "X" and board[i][0] == " "):
                        put_in_board(board, "O", i*3+1)
                        break
                    elif (board[0][i] == board[1][i] == "X" and board[2][i] == " "):
                        put_in_board(board, "O", 6+i+1)
                        break
                    elif (board[0][i] == board[2][i] == "X" and board[1][i] == " "):
                        put_in_board(board, "O", 3+i+1)
                        break
                    elif (board[1][i] == board[2][i] == "X" and board[0][i] == " "):
                        put_in_board(board, "O", i+1)
                        break
                    else:
                        make_random_move(board, "O")
                        break


            print_board_and_legend(board)  
            filled_spots+=1

            if is_win(board, "O"):
                print("Computer wins!")
                game_over = True





            

                
