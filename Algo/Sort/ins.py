def insertion(A):
	for i in range(1, len(A)):
		key = A[i]
		j = i - 1
		while A[j] > key and j >= 0:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = key
	return A


print(insertion([5, 4, 3,2,1]))