A = 'AB'

def titleToNumber(A):
	#65 = 'A'
	N = len(A)
	code = 0
	k = 0
	for i in range(N - 1, -1, -1):
		code += (ord(A[i]) - 64) * (26 ** k)
		k += 1
	return code

print(titleToNumber(A))



