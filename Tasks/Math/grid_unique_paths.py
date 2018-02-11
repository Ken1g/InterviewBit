def uniquePaths(A, B):
	ans = []
	for i in range(A):
		ans.append([0])
	for i in range(1, B + 1):
		ans[0].append(1)
	for i in range(1, A):
		for j in range(1, B + 1):
			ans[i].append(ans[i][j - 1] + ans[i - 1][j])
	return ans[A - 1][B]


print(uniquePaths(3, 3))			
