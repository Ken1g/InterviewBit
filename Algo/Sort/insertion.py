A = [1, -4, 4, 6, 8, 3, 9, 0, 9]

def insertion_sort(A):
	for i in range(1, len(A)):
		key = A[i]
		j = i - 1
		while j >= 0 and A[j] > key:
			A[j + 1] = A[j]
			j -= 1 
		A[j + 1] = key
	return A

print(A)
print(insertion_sort(A))
		
