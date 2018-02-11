A = [1, 2, 3, 4, 5, 6]

def wave(A):
	A.sort()
	ans = []
	for i in range(0, len(A), 2):
		ans.append(A[i])
	for i in range(1, len(A), 2):
		ans.insert(i - 1, A[i])
	return(ans)

print(wave(A))
	
