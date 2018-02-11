A = []
B = 8

print A

def firstSearch(A, B):
	if len (A) == 0:
		return -1
	start = 0
	end = len(A)
	while start <= end:
		mid = (start + end) / 2
		if mid != 0:
			if mid >= len(A):
				return -1
			if A[mid] == B and A[mid - 1] != B:
				return mid
			elif A[mid] < B:
				start = mid + 1
			else:
				end = mid - 1
		else:
			if A[mid] == B:
				return 0
			elif A[mid] > B:
				return -1
			else:
				start = mid + 1
	return -1

def secondSearch(A, B):
	if len(A) == 0:
		return -1
	start = 0
	end = len(A)
	while start <= end:
		mid = (start + end) / 2
		if mid != len(A) - 1:
			if A[mid] == B and A[mid + 1] != B:
				return mid
			elif A[mid] > B:
				end = mid - 1
			else:
				start = mid + 1
		else:
			if A[mid] == B:
				return len(A) - 1
			elif A[mid] < B:
				return -1
			else:
				end = mid - 1
	return -1

def searchRange(A, B):
	ans = []
	ans.append(firstSearch(A, B))
	ans.append(secondSearch(A, B))
	return ans
	

print(searchRange(A, B))
