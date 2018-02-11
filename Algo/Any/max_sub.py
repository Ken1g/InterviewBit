import math
import numpy as np

def find_cross(A, l, m, h):
	l_sum = - np.inf
	r_sum = - np.inf
	S = 0
	for i in range(m, h + 1, 1):
		S += A[i]
		if S >= r_sum:
			r_sum = S
			r = i
	S = 0
	for i in range(m, l - 1, - 1):
		S += A[i]
		if S >= l_sum:
			l_sum = S
			l = i
	return l, r, l_sum + r_sum - A[m]

def find_sub(A, l, h):
	if l == h:
		return (l, h, A[l])
	else:
		m = (l + h) // 2
	(l_l, l_r, l_s) = find_sub(A, l, m)
	(r_l, r_r, r_s) = find_sub(A, m + 1, h)
	(m_l, m_r, m_s) = find_cross(A, l, m, h)
	if (l_s >= r_s) and (l_s >= m_s):
		return (l_l, l_r, l_s)
	elif (r_s >= l_s) and (r_s >= m_s):
		return (r_l, r_r, r_s)
	else:
		return (m_l, m_r, m_s)

A = [-50000000000]
l, r, ans = find_sub(A, 0, len(A) - 1)
print(ans)
