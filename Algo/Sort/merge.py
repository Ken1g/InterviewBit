import numpy 	as np
import math 	as mt

def merge(A, st, mid, fin):
	n_l = mid - st + 1
	n_r = fin - mid
	L = []
	R = []
	for i in range(n_l):
		L.append(A[st + i])
	for i in range(n_r):
		R.append(A[mid + i + 1])
	L.append(np.inf)
	R.append(np.inf)
	j = k = 0
	for i in range(st, fin + 1):
		if L[j] < R[k]:
			A[i] = L[j]
			j += 1
		else:
			A[i] = R[k]
			k += 1
		 

def merge_sort(A, st, fin):
	if st != fin:
		mid = (st + fin) // 2
		merge_sort(A, st, mid)
		merge_sort(A, mid + 1, fin)
		merge(A, st, mid, fin)

#	MAIN

N = input("N = ")
A = []
for i in range(N):
	A.append(input())
if N > 0:
	merge_sort(A, 0, N - 1)
print(A)		
