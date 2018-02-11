A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def rotate(A):
	N = len(A)
	for i in range(N // 2 + N % 2):
		for j in range(i, N - i - 1):
			mem = A[i][j]
			A[i][j] = A[N - j - 1][i]
			A[N - j - 1][i] = A[N - i - 1][N - j - 1]
			A[N - i - 1][N - j - 1] = A[j][N - i - 1]
			A[j][N - i - 1] = mem
	return A

print(rotate(A))
			
			
		
