# Print out lal passwords over an alphabet

def print_all(alphabet, n, start_str = ""):
    '''Print all combinations of elements of alphabet of length n, with string start_str prepended

    >> print("abc", 2, "zz")
    zzaa
    zzab
    zzac
    zzba
    zzbb
    zzbc
    zzca
    zzcb
    zzcc
    '''

    if n == 0:
        print(start_str)
        return

    for letter in alphabet:
        print_all(alphabet, n-1, start_str + letter)

'''Complexity

0, "aaa"    0, "aab"    0, "aac"
    \  | /
    1, "aa"    1, "ab"  1,"ac"                             #3^2
        \       |     /
        "abc",2,"a"     "abc", 2, "b"       "abc",2, "c"   #3^alphabet
            \                   |                 /
                        "abc", 3, ""
        '''
#len(alphabet): m
#length of the string generated : n

#complextiy: 1 + m + m^2 + ... m^2 = m^n+1 -1/ m-1

#total runtime: O(m * (m^n+1 - 1/ m-1) = O(m^n+1)

def all_combinations(alphabet, n, start_str = ""):
    '''Return all combinations of elements of alphabet of length n, with string start_str prepended
    '''

    if n == 0:
        return [start_str]

    res = []
    for letter in alphabet:
        res.extend(all_combinations(alphabet, n-1, start_str + letter))
    return res
