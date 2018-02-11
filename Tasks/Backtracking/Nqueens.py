class Solution:
	def solveNQueens(self, A):
		ans = []
		start = []
		rows = []
		columns = []
		diag1 = []
		diag2 = []
		for i in range(A):
			rows.append(True)
			columns.append(True)
			diag1.append(True)
			diag1.append(True)
			diag2.append(True)
			diag2.append(True)
		self.queenRow(start, 0, A, ans, rows, columns, diag1, diag2)
		return ans

	def queenRow(self, start, n, A, ans, rows, columns, diag1, diag2):
		if n == A:
			ans.append(start)
		else:
			for i in range(A):
				new_start = start[:]
				new_rows = rows[:]
				new_columns = columns[:]
				new_diag1 = diag1[:]
				new_diag2 = diag2[:]
				if columns[n] and rows[i] and diag1[n + i] and diag2[n - i + A - 1]:
					string = "." * i
					string += "Q"
					string += "." * (A - i - 1)
					new_start.append(string)
					new_rows[i] = False
					new_columns[n] = False
					new_diag1[n + i] = False
					new_diag2[n - i - 1 + A] = False
					self.queenRow(new_start, n + 1, A, ans, new_rows, new_columns, new_diag1, new_diag2)






sol = Solution()
A = 5
print(sol.solveNQueens(A))
