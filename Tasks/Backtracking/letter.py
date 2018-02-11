class Solution:
        def letterCombinations(self, A):
		l = []
		l.append(["0"])
		l.append(["1"])
		l.append(["a", "b", "c"])
		l.append(["d", "e", "f"])
		l.append(["g", "h", "i"])
		l.append(["j", "k", "l"])
		l.append(["m", "n", "o"])
		l.append(["p", "q", "r", "s"])
		l.append(["t", "u", "v"])
		l.append(["w", "x", "y", "z"])
		ans = []
		
		self.put(A, 0, ans, "", l)
		return ans

	def put(self, A, k, ans, start, l):

		if k == len(A):
			ans.append(start)
			return
		num = ord(A[k]) - 48
		for i in l[num]:
			curr = start
			curr += i
			self.put(A, k + 1, ans, curr, l)
		
			
		
sol = Solution()
A = "23"
print(sol.letterCombinations(A))
