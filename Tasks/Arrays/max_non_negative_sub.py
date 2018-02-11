A = [1, 2, 5, -7, 4, 5, 10, -443, 34234324, 43]
import numpy

def maxset(A):
	A.append(- numpy.inf)
	in_sub = 0
	max_sum = length = -2
	S = L = 0
	for i in range(len(A)):
		if A[i] < 0:
			if in_sub == 1:
				in_sub = 0
				if S > max_sum:
					max_sum = S
					length = L
					start = St 
					index = i_St
				elif S == max_sum:
					if L > length:
						max_sum = S
						length = L
						start = St
						index = i_St
					elif L == length:
						if St < start:
							max_sum = S
							length = L
							start = St
							index = i_St
			S = 0
			L = 0
		else:
			if in_sub == 0:
				in_sub = 1
				S += A[i]
				L += 1
				St = A[i]
				i_St = i
			else:
				S += A[i]
				L += 1
	ans = []
	for i in range(length):
		ans.append(A[index + i])
	return ans

print(maxset(A))
