def counting_sort(A):
	C = []
	for i in range(len(A)):
		C.append(0)
	B = C[:]
	for j in range(len(A)):
		C[A[j]] += 1
	for i in range(1, len(A)):
		C[i] += C[i - 1]
	for j in range(len(A) - 1, -1, -1):
		B[C[A[j]] - 1] = A[j]
		C[A[j]] -= 1
	return B

print(counting_sort([0, 5, 4, 3, 1, 2]))
