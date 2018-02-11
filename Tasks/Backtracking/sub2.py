class Solution:
        def subsetsWithDup(self, A):
                A.sort()
                ans = []
                start = []
                self.create_sub(A, ans, 0, start)

                return ans

        def create_sub(self, A, ans, k, start):
                ans.append(start)
                for i in range(k, len(A)):
			if i == 0 or i == k or A[i] != A[i - 1]:
                       		cur = start[:]
                        	cur.append(A[i])
                        	self.create_sub(A, ans, 1 + i, cur)

			
		







sol = Solution()
A = [1, 2, 2]
print(sol.subsetsWithDup(A))
