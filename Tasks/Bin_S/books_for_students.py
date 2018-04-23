class Solution:
	def books(self, A, B):
		start = max(A)
		end = sum(A)

	#	if B < start:
	#		return -1
		if len(A) < B:
			return -1
		while end >= start:
			mid = (start + end) // 2
			st = self.count_students(mid, A)
			if st >= B:
				start = mid + 1
			else:
				end = mid - 1

		return start





	def count_students(self, m, P):
		summ = 0 
		count = 0
		for i in P:
			summ += i
			if summ > m:
				summ = i
				count += 1
		return count

sol = Solution()
print(sol.books([0, 4, 4], 2))


