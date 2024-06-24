def longest_run2(s, ch):
    # at most len(s) times
    for longest in range(len(s), -1, -1):
        cur_run = 0

        #The loop below takes at most len(s) * const operations
        #runs at most len(s) times
        for i in range(len(s)):
            #takes at most const opperations
            if s[i] == ch:
                cur_run += 1
            else:
                cur_run = 0

            if cur_run == longest:
                return longest
    return 0

#Analyze Runtime: at most: len(s) * len(s) * const operations
#Run time: O(n^2)m where n = len(s)
