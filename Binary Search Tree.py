# Python3 implementation of the approach
import math
# Maximum number of vertices
N = 985
# To store is it possible at
# particular pace or not
dp = [[[-1 for z in range(2)]
       for e in range(N)]
      for f in range(N)]

# Return 1 if from l to r, it is
# possible with the given state
def possibleWithState(l, r, state, a):
    # Base condition
    if (l > r):
        return 1

    # If it is already calculated
    if (dp[l][r][state] != -1):
        return dp[l][r][state]

    # Choose the root
    root = 0
    if (state == 1):
        root = a[r + 1]
    else:
        root = a[l - 1]

    # Traverse in range l to r
    for i in range(l, r + 1):

        # If gcd is greater than one
        # check for both sides
        if (math.gcd(a[i], root) > 1):
            e = possibleWithState(l, i - 1, 1, a)
            if (e != 1):
                continue
            f = possibleWithState(i + 1, r, 0, a)
            if (e == 1 and f == 1):
                return 1

    # If not possible
    return 0

# Function that return true if it is
# possible to make Binary Search Tree
def isPossible(a, n):
    # Sort the given array
    a.sort()

    # Check it is possible rooted at i
    for i in range(n):

        # Check at both sides
        if (possibleWithState(0, i - 1, 1, a) and
                possibleWithState(i + 1, n - 1, 0, a)):
            return True
    return False

# Driver Code
if __name__ == '__main__':
    a = [5, 8, 11, 18, 34, 120]
    n = len(a)
    if (isPossible(a, n)):
        print("Yes")
    else:
        print("No")
