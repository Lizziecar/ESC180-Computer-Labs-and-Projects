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

def get_coord(square_num): #broken right now
    coord =  [0,0] #create a list
    coord[0] = (square_num -1) // 3 #formula for row

    print(square_num)

    #column
    if square_num == 1 or square_num == 4 or square_num == 7:
        coord[1] = 0
    if square_num == 2 or square_num == 5 or square_num == 8:
        coord[1] = 1
    if square_num == 3 or square_num == 6 or square_num == 9:
        coord[1] = 2
    '''else:
        print("Value is not available")'''

    return coord

#to make it easier
def get_X_or_O(board,coord1,coord2):
    if board[coord1][coord2] == "X":
        return "X"
    if board[coord1][coord2] == "O":
        return "O"
    if booard[coord1][coord2] == None:
        return None

def put_in_board(board, mark, square_num):
    coords = get_coord(int(square_num))

    board[coords[0]][coords[1]] = mark

def get_free_squares(board):
    free_squares = []
    for i in range(9):
        coords = get_coord(i)
        if board[coords[0]][coords[1]] == None:
            free_squares.append(coords)

    return free_squares



if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    '''print("\n\n")

    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]

    print_board_and_legend(board)'''

    place_input = ""
    while place_input != " ":
        place_input = input("Enter location for X: ")
        put_in_board(board, "X", place_input)
        print_board_and_legend(board)

        place_input = input("Enter location for O: ")
        put_in_board(board, "O", place_input)
        print_board_and_legend(board)

