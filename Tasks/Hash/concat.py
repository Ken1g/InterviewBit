S = "barfoothefoobarman"
L = ["foo", "bar"]

class Solution:
	def findSubstring(self, A, B):
		import copy
		dic = {}
		lenb = len(B[0])
		for x in B:
			if x in dic:
				dic[x] += 1
			else:
				dic[x] = 1
		copy_dic = copy.deepcopy(dic)		
		ans = set()
		for j in range(len(A) - len(B) * lenb + 1):
			for k in range(len(B)):
				curr_w = A[(j + k * lenb) : (j + (k + 1) * lenb)]
				if curr_w in copy_dic:
					copy_dic[curr_w] -= 1
					if copy_dic[curr_w] == 0:
						del copy_dic[curr_w]
			if copy_dic == {}:
				ans.add(j)
			copy_dic = copy.deepcopy(dic)
		return(list(ans))


			
sol = Solution()
print(sol.findSubstring(S, L))
			
