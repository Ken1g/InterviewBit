class Solution:
	def fibsum(self, A):
		arr = []
		self.generate_Fibs(arr, A)
		sum = 0
		num = 0
		pointer = len(arr) - 1
		while sum != A:
			if arr[pointer] > (A - sum):
				pointer -= 1
			else:
				sum += arr[pointer]
				num += 1

		return num
		


	def generate_Fibs(self, arr, A):
		cur = 1
		next = 2
		while cur <= A:
			arr.append(cur)
			t = next
			next += cur
			cur = t

sol = Solution()
A = 120	
print(sol.fibsum(A))
