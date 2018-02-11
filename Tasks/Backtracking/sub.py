class Solution:
        def subsets(self, A):
                A.sort()
                ans = []
                start = []
                self.create_sub(A, ans, 0, start)
		
		return ans

        def create_sub(self, A, ans, k, start):
                ans.append(start)
		for i in range(k, len(A)):
                        cur = start[:]
                        cur.append(A[i])
			self.create_sub(A, ans, 1 + i, cur)  









sol = Solution()
A = [1, 2, 3]
#A = [15, 20, 12, 9, 4]
print(sol.subsets(A))
