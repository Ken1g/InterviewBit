class Solution:
	def permute(self, A):
		ans = []
		self.add(A, [], ans)
		return ans

	def add(self, B, seq, ans):
		if len(B) == 1:
			seq.append(B[0])
			ans.append(seq)
		else:
			for i in range(len(B)):
				C = B[:]
				new_seq = seq[:]
				new_seq.append(B[i])
				del C[i]
				self.add(C, new_seq, ans)	
		






sol = Solution()
A = [1, 2, 3, 4]
print(sol.permute(A))







