class Solution:
	def searchMatrix(self, A, B):
		line_s = 0
		line_f = len(A) - 1
		line = -1
		column_s = 0
		column_f = len(A[0]) - 1
		column = -1
		while line_s <= line_f:
			mid = (line_f + line_s) // 2
			if B < A[mid][0]:
				line_f = mid - 1
			elif B > A[mid][-1]:
				line_s = mid + 1

			else:
				line = mid
				break
		if line == -1:
			return 0

		while column_s <= column_f:
			mid = (column_f + column_s) // 2
			if B < A[line][mid]:
				column_f = mid - 1
			elif B > A[line][mid]:
				column_s = mid + 1
			else:
				column = mid
				break
		if column == -1:
			return 0
		else:
			return 1

sol = Solution()
A =[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

B = 1
print(sol.searchMatrix(A, 1))
print(sol.searchMatrix(A, 3))
print(sol.searchMatrix(A, 5))
print(sol.searchMatrix(A, 7))
print(sol.searchMatrix(A, 10))
print(sol.searchMatrix(A, 11))
print(sol.searchMatrix(A, 16))
print(sol.searchMatrix(A, 20))
print(sol.searchMatrix(A, 23))
print(sol.searchMatrix(A, 30))
print(sol.searchMatrix(A, 34))
print(sol.searchMatrix(A, 50))
print(sol.searchMatrix(A, 54))
print(sol.searchMatrix(A, 8))

