class Solution:
	def wordBreak(self, A, B):
		table = {}
		for wd in B:
			table[wd] = True

		L = len(A)
		word = [[0 for _ in range(L)] for _ in range(L)]
		ans = []
		current_string = ""
		self.string_parser(word, current_string, 0, ans, A, table)
		return ans

	def string_parser(self, word, current_string, position, ans, A, table):
		wd = ""
		start_pos = position
		cur_string = current_string
		while True:
			if position == len(A):
				break
			wd += A[position]
			if word[start_pos][position] == 0:
				if table.get(wd, None) != None:
					word[start_pos][position] = wd
				else:
					word[start_pos][position] = None
			if word[start_pos][position] != None:
				add = ""
				if cur_string != "":
					add = " "
				new_string = cur_string + add + wd
				if position != len(A) - 1:
					self.string_parser(word, new_string, position + 1, ans, A, table)
				else:
					ans.append(new_string)

			position += 1


A = "catsanddog"
B = ["cat", "cats", "sand", "and", "dog"]
sol = Solution()
print(sol.wordBreak(A, B))