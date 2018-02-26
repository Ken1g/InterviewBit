class Solution:
	def wordBreak(self, A, B):
		table = {}
		for wd in B:
			table[wd] = True

		L = len(A)
		word = [[0 for _ in range(L)] for _ in range(L)]
		ans = [0]
		found = [0]
		self.string_parser(word, 0, ans, A, table)
		return ans[0]

	def string_parser(self, word, position, ans, A, table):
		if ans[0] == 1:
			return
		wd = ""
		start_pos = position
		while True:
			if ans[0] == 1:
				return
			if position == len(A):
				break
			wd += A[position]
			if word[start_pos][position] == 0:
				if table.get(wd, None) != None:
					for i in range(position + 1):
						word[i][position] = None
					word[start_pos][position] = True
				else:
					word[start_pos][position] = None
			if word[start_pos][position] != None:
				if position != len(A) - 1:
					self.string_parser(word, position + 1, ans, A, table)
				else:
					ans[0] = 1

			position += 1


A = "aaaabbbbababbaaabbbabbabaaabbaaaabbababbaabababaabbbababaaababbbbbaaababababbbbbaaaabbabbabaabbababbaaaaabbaababababbbaaaabaaabaabaababbabaaabaaababababbaabbbbbaabbabbaaaaabbabbbabbbbaaaaabababbaababbabbbabbbababaabaababbbaaaaababababbaabaabaabbbbaaabbbbbbababbabbabaabbaababbbbbbabaababbbbababbabbbbbbabbbbbbaabbbbbbabaabbabaabbbaaaababaababbbabaabbbbabbbbbbbababbaabbbaaabaabaabaabbbab"
B = [ "bbabaaaaba", "abbaa", "bbabbaaba", "bbaabbab", "ab", "b", "abaaaababa", "aa", "babaa", "aaa", "baa", "ab", "baaabbbba", "aaaba", "a", "bbaababaab", "baaaaaaa", "aaab", "bbabbbbaaa", "ab", "aaa", "bbb", "a", "bab", "aaaaaa", "aa", "b", "ababaabbb", "bbb", "babbbbba", "bbabb", "ab", "a", "baabaabbb", "aaabab", "aba", "a", "babba", "aaaababbbb", "b", "baab", "baabbbb", "babbb", "ababaa", "babbaa", "abaaa", "babababab", "bab", "aa", "abbaa", "abb", "bbbaaaaba", "bbbabababb", "aaaa", "ba", "bbaabbbaab", "bababb", "bbbb", "baaabbaab", "bababbbaaa", "bbaab", "ab", "bbbaaa", "aaaa", "aab", "baabaabaa", "bb", "ba", "bbbb", "abbaababab", "baaaaaa", "baaabbbb", "baab" ]
sol = Solution()
print(sol.wordBreak(A, B))








#EDITORIAL
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        if not wordDict:
            return 0
        aux = [0]*(len(s) + 1)
        aux[0] = 1
        for i in xrange(len(s)):
            for j in xrange(i, -1, -1):
                if aux[j] and s[j : i + 1] in wordDict:
                    aux[i + 1] = 1
                    break

        return aux[len(s)]
