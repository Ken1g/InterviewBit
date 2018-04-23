class Solution:
	def searchInsert(self, A, B):
		start = 0
		end = len(A) - 1
		mid = end
		while start <= end:
			mid = (start + end) // 2
			if A[mid] == B:
				return mid
			elif A[mid] > B:
				end = mid - 1
			else:
				start = mid + 1
		return start

sol = Solution()
print(sol.searchInsert([1, 5, 6, 9], 8))
print(sol.searchInsert([], 4))