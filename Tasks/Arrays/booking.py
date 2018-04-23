class Solution:
	def hotel(self, arrive, depart, K):
		N = len(arrive)
		points = []
		for i in range(N):
			points.append((arrive[i], 1))
			points.append((depart[i], 0))
		points.sort()
		guests = 0
		print(points)
		for i in points:
			if not i[1]:
				guests -= 1
			else:
				guests += 1
				if guests > K:
					return False
		return True



sol = Solution()
arrive = [1, 2, 3]
depart = [2, 3, 4]
K = 1
print(sol.hotel(arrive, depart, K)) 
