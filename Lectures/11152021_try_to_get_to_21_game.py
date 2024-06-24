# Start from 0
# Each plater can say either +1 pr +2
# The first player to get to the sum 21, wins the game

def is_winning_sum(s):
    if s == 21:
        return True

    MOVES = [1,2]
    # if is_winning_sum(s+1) is True of is_winning_sum(s+2) is True
    #, then is_winning(s) ,must be False

    for move in MOVES:
        if is_winning_sum(s+move):
            return False
    return True
