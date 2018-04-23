class Solution:
	def findRank(self, A):
		to_sort = []
		for idx, letter in enumerate(A):
			to_sort.append((ord(letter), idx))
		to_sort.sort()

		positions = {}
		for idx, letter in enumerate(to_sort):
			positions[letter[1]] = idx + 1
		ans = 0
		used = {}
		import math
		for idx, i in enumerate(A):
			position = positions[idx]
			fact = math.factorial(len(A) - idx - 1)
			const = position - 1
			for j in range(position - 1):
				if used.get(j + 1, None) != None:
					const -= 1
			used[position] = True
			ans += fact * const
		return (ans + 1) % 1000003




sol = Solution()
print(sol.findRank("a"))



