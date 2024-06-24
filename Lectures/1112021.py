def longest_run1(s, c):
    #const runtime
    run = 0
    max_run = 0

    if c == "z":
        s += "y"
    else:
        s += "z"

    #const run time multiplied by len(s)
    for ch in s:
        if ch != c:
            max_run = max(run, max_run)
            run = 0
        else:
            run += 1

    return max_run

#Runtime: const1 + len(s) * const2
#          O(n), n = len(s)