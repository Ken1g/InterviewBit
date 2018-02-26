class Solution:
	def seats(self, A):
		pos = []
		MOD = 10000003
		for idx, el in enumerate(A):
			if el == "x":
				pos.append(idx)

		N = len(pos)
		if N == 0:
			return 0
		start = pos[N // 2] - N // 2
		ans = 0
		position = start
		for i in pos:
			ans = (ans + abs(position - i)) % MOD
			position += 1

		return ans



		


sol = Solution()
A = "....x..xx...x.."
print(sol.seats(A))