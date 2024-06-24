"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 30, 2021
"""

def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != " ":
                return False
    return True

def is_full(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                return False
    return True



def is_bounded(board, y_end, x_end, length, d_y, d_x):
    #endpoint
    #startpoint
    length -= 1

    #check endpoint
    if x_end + d_x > 7 or y_end + d_y > 7 or x_end + d_x < 0 or y_end + d_y < 0:
        endpoint = "CLOSED"
    elif board[y_end + d_y][x_end + d_x] != " ":
        endpoint = "CLOSED"
    else:
        endpoint = "OPEN"

    #check startpoint
    start_x = x_end - (d_x * (length))
    start_y = y_end - (d_y * (length))
    if  start_x - d_x > len(board) - 1 or start_y - d_y > len(board) - 1 or start_x - d_x < 0 or start_y - d_y < 0: #startpoint is edge
        startpoint = "CLOSED"
    elif board[start_y - d_y][start_x - d_x] != " ": #startpoint is closed
        startpoint = "CLOSED"
    else:
        startpoint = "OPEN"

    #compare results
    if endpoint == startpoint:
        return endpoint
    else:
        return "SEMIOPEN"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    y_val = y_start
    x_val = x_start
    open_seq_count = 0
    semi_open_seq_count = 0

    #create list of row
    x_values = []
    y_values = []
    while x_val >= 0 and x_val <= 7 and y_val >= 0 and y_val <= 7:
        x_values.append(x_val)
        y_values.append(y_val)

        x_val += d_x
        y_val += d_y

    #create list of colours in row
    colours_in_row = []
    for i in range(len(x_values)):
        n = x_values[i]
        m = y_values[i]

        if board[m][n] == "b":
            colours_in_row.append("b")
        elif board[m][n] == "w":
            colours_in_row.append("w")
        else:
            colours_in_row.append(" ")


    #find start point of row
    for i in range(len(colours_in_row)):
        if colours_in_row[i] == col:
            #find end point of row
            endpoint = i + (length-1)
            if endpoint <= len(colours_in_row) - 1 and endpoint >= 0: #make sure endpoint is within board
                if colours_in_row[endpoint] == col:
                    #check if row is complete:
                    row_complete = True #marker if row is complete
                    for k in range(i+1, endpoint):
                        if colours_in_row[k] != col: #there's a hole
                            row_complete = False
                    #check if the row is not actually size length
                    #start
                    if i > 0:
                        if colours_in_row[i-1] == col:
                            row_complete = False

                    #end
                    if endpoint < (len(colours_in_row)-1):
                        if colours_in_row[endpoint + 1] == col:
                            row_complete = False

                    if row_complete == True:
                        #row exists and is the proper length
                        #find coordinates
                        end_x = x_values[endpoint]
                        end_y = y_values[endpoint]

                        open_or_semi = is_bounded(board, end_y, end_x, length, d_y, d_x)
                        if open_or_semi == "OPEN":
                            open_seq_count += 1
                        if open_or_semi == "SEMIOPEN":
                            semi_open_seq_count += 1

    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    directions = [[0,1],
                  [1,0],
                  [1,1],
                  [1,-1]]

    #prevent repeating: check [0,0] in the direction of 0[right]
    open_sequences, semi_open_sequences = detect_row(board, col, 0, 0, length, directions[0][0], directions[0][1])
    open_seq_count += open_sequences
    semi_open_seq_count += semi_open_sequences

    #prevent repeating: check [0,0] in the direction of 0[down]
    open_sequences, semi_open_sequences = detect_row(board, col, 0, 0, length, directions[1][0], directions[1][1])
    open_seq_count += open_sequences
    semi_open_seq_count += semi_open_sequences

    #the rest of the points
    #horizontal axis:
    for i in range(len(board)):
        for j in [1,2,3]:
            open_sequences, semi_open_sequences = detect_row(board, col, 0, i, length, directions[j][0], directions[j][1])
            open_seq_count += open_sequences
            semi_open_seq_count += semi_open_sequences

    #vertical axis:
    for i in range(1, len(board)):
        for j in [0,2,3]:
            open_sequences, semi_open_sequences = detect_row(board, col, i, 0, length, directions[j][0], directions[j][1])
            open_seq_count += open_sequences
            semi_open_seq_count += semi_open_sequences

    #specically [1,-1] sequences below the seven diagonal
    for i in range(1, len(board)):
        open_sequences, semi_open_sequences = detect_row(board, col, i, 7, length, directions[3][0], directions[3][1])
        open_seq_count += open_sequences
        semi_open_seq_count += semi_open_sequences

    return open_seq_count, semi_open_seq_count

def search_max(board):
    current_score = score(board)
    move_y = 0
    move_x = 0

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == " ":
                #place test spot
                board[i][j] = "b"
                test_score = score(board)

                if test_score >= current_score:
                    current_score = test_score
                    move_y = i
                    move_x = j

                board[i][j] = " "

    print(move_y,move_x)
    return move_y, move_x

def score(board): #don't change
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
    b_open5, b_semi_open5 = detect_rows(board, "b", 5)
    if b_open5 >= 1 or b_semi_open5 >= 1:
        return "Black won"
    w_open5, w_semi_open5 = detect_rows(board, "w", 5)
    if w_open5 >= 1 or w_semi_open5 >= 1:
        return "White won"
    if is_full(board) == True:
        return "Draw"

    return "Continue playing"


def print_board(board): #don't change

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



def analysis(board): #don't change
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))






def play_gomoku(board_size): #don't change
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

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
        analysis(board)

        game_res = is_win(board)
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



def put_seq_on_board(board, y, x, d_y, d_x, length, col): #don't change
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

    y_end = y + (length-1)*d_y
    x_end = x + (length-1)*d_x

    print(y_end,x_end)

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 1; y = 3; d_x = 1; d_y = 0; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 6; y = 3; d_x = 1; d_y = 0; length = 2
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    print_board(board)
    if detect_row(board, "w", 3,0,2,d_y,d_x) == (0,1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 1; y = 2; d_x = 1; d_y = -1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 5; y = 2; d_x = 1; d_y = -1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 3; y = 6; d_x = 1; d_y = -1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 4; y = 7; d_x = 1; d_y = -1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    print_board(board)
    if detect_rows(board, col,3) == (1,3):
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

    print_board(board)

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




if __name__ == '__main__':
    pass
    play_gomoku(8)
