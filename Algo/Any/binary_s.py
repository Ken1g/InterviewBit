def bin_s(A, x):
	start = 0
	end = len(A)
	while start <= end:
		mid = (start + end) / 2
		if A[mid] == x:
			return mid
		elif A[mid] < x:
			start = mid + 1
		else:
			end = mid - 1
	return - 1

A = [1, 4, 6, 7, 8, 9]
print(bin_s(A, 9))
		
