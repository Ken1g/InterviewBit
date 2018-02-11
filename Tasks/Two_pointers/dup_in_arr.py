A = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9]

def removeDuplicates(A):
	i = 0	
	j = 0
	A.append(999999999999999)
	if len(A) == 1:
		return 0
	while True:
		if j == len(A):
			break
		if A[j] > A[i]:
			A[(i + 1):j] = []
			i += 1
			j = i
		else:
			j += 1
		
	return len(A) - 1


print(removeDuplicates(A))
print A
