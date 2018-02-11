import math
import numpy as np

A = [0]

def plusOne(A):
	zeros = 1
        while (zeros == 1):
        	if (len(A) == 0) or (A[0] != 0):
                    	zeros = 0
            	else:
                	del A[0]
	A.reverse()
	A.append(0)
	end = 0
	i = 0
        while (end == 0):
		if A[i] == 9:
			A[i] = 0
			i += 1
		else:
			A[i] += 1
			end = 1
	A.reverse()
	if A[0] == 0:
		del A[0]

	return(A)
			
		

print(plusOne(A))
