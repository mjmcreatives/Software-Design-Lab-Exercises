def GET_THE_MAX(S, index):
    if index == len(S) - 1:
        return S[index]
    return max(S[index], GET_THE_MAX(S, index + 1))


def find_max(S):
    return GET_THE_MAX(S, 0)


print(find_max([10, 20, 30, 40, 50, 60, 70, 80, 90, 99]))
print(find_max([124, 567, 894, 231, 451, 789, 89, 678, 134]))
print(find_max([45, 78, 43, 12, 69, 37, 224, 121, 543]))
