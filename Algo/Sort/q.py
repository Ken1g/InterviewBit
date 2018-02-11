A = [0, -4, 5, 35, 7, 6]

def qsort(A, p, r):
	if p < r:
		q = partition(A, p, r)
		qsort(A, p, q - 1)
		qsort(A, q + 1, r)

def partition(A, p, r):
	x = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j] <= x:
			i = i + 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[r] = A[r], A[i + 1]
	return i + 1 

qsort(A, 0, len(A) - 1)	
print(A)
