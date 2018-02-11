A = [[0, 1, 1], [1, 0, 0], [1, 1, 1]]

def setZeros(A):
	m = len(A)
	n = len(A[0])
	row = True
	column = True
	for i in range(0, n):
		if A[0][i] == 0:
			row = False
			break
	for i in range(0, m):
		if A[i][0] == 0:
			column = 0
			break
	for i in range(1, m):
		for j in range(1, n):
			if A[i][j] == 0:
				A[0][j] = 0
				A[i][0] = 0
	for i in range(1, n):
		if A[0][i] == 0:
			for j in range(1, m):
				A[j][i] = 0
	for i in range(1, m):
		if A[i][0] == 0:
			for j in range(1, n):
				A[i][j] = 0
	if column == 0:
		for i in range(0, m):
			A[i][0] = 0
	if row == 0:
		for i in range(0, n):
			A[0][i] = 0
	return A

print(A)
print(setZeros(A))
			
