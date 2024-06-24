# L = [4, 2, 3]
# All the subsets of L
# [[]m [4], [2], [3], [2,4], ..... [4, 2, 3]

def get_all_subsets(L):
    if len(L) == 0:
        return [[]]

    #Two kinsd of subsets of L: those that contain L[0] and those that don't

    #[L[0], ....]
    # [.....] # no L[0] -> get_all_subsets(L[1:])
    all0 = get_all_subsets(L[1:])
    res = []
    for subset in all0:
        res.append(L[0] + subset)
    res.extend(all0)
    return res