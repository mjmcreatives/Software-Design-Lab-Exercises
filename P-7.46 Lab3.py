def GET_THE_MAX(S, index):
    if index == len(S) - 1:
        return S[index]
    return max(S[index], GET_THE_MAX(S, index + 1))


def find_max(S):
    return rec_find_max(S, 0)


print(find_max([1, 2, 3, 4, 5, 6, 7, 8]))
print(find_max([1, 2, 774, 5, 6, 7, 8]))
print(find_max([8, 7, 6, 5, 4, 3, 2, 1]))
