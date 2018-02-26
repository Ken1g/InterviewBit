class Solution:
	def maxp3(self , A):
		A.sort()
		A.reverse()
		return(max(A[0] * A[1] * A[2], A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1], A[-1] * A[-2] * A[0]))





sol = Solution()
A = [0, -1, 3, 100, 7, 50]
print(sol.maxp3(A))