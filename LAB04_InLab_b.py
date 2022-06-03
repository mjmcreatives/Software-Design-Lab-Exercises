def multrecur(n, m) :

# case 1 : n<0 and m>0
	# swap the position of n and m to keep second
	# parameter positive
	if n > 0 and m < 0 :
		return multrecur(m,n)

	# case 2 : both n and m are less than 0
	# return the product of their absolute values
	elif n < 0 and m < 0 :
		return multrecur((-1 * n),(-1 * m))

	# if n>m , swap n and m so that recursion
	# takes less time
	if n > m :
		return multrecur(m, n)

	# as long as m is not 0 recursively call multrecur for
	# n and m-1 return sum of n and the product of n times m-1
	elif m != 0 :
		return n + multrecur(n, m-1)

	# m=0 then return 0
	else :
		return 0
# Driver Code
if __name__ == "__main__" :

	print("9 * 7 =",multrecur(9, 7))
	print("3 * (5) =",multrecur(3, 5))
	print("(8) * 4 =",multrecur(8, 4))
