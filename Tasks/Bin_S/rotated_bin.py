A = [4]
B = 5

class Solution():
	def search(self, A, B):
		if len(A) == 0:
			return -1
		min1 = A[0]
		max2 = A[len(A) - 1]
		if B == min1:
			return 0
		elif B == max2:	
			return len(A) - 1
		start = 0
		end = len(A) - 1
		if B > min1:
			while start <= end:
				mid = (start + end) / 2
				if A[mid] < min1:
					end = mid - 1
				elif A[mid] == B:
					return mid
				elif A[mid] < B:
					start = mid + 1
				else:
					end = mid - 1
		else:
			while start <= end:
				mid = (start + end) / 2
				if A[mid] > max2:
					start = mid + 1
				elif A[mid] == B:
					return mid
				elif A[mid] < B:
					start = mid + 1
				else:
					end = mid - 1
		return - 1
		


sol = Solution()
print(sol.search(A, B))
