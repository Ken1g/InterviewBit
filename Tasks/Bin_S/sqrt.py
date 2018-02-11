def sqrt(A):
	start = 0
	end = A
	old = -1
	if A == 1:
		return 1
	while start <= end:
		mid = (start + end) / 2
		if old == mid:
			return mid
		else:
			old = mid
		if mid * mid == A:
			return mid
		elif mid * mid < A:
			start = mid
		else:
			end = mid

A = 0
print(sqrt(A))
		
