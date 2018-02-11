intervals = [[-100, -50], [50, 100]]
new_interval = [-2, 20]


def is_overlap(A, B):
	if max(A[0], B[0]) > min(A[1], B[1]):
		return False
	else:
		return True

def insert(intervals, new_interval):
	if len(intervals) == 0:
		intervals.append(new_interval)
		return intervals
	if new_interval[0] > new_interval[1]:
		new_interval[1], new_interval[0] = new_interval[0], new_interval[1]
	start 	= False
	finish 	= False
	kill = []
	for idx, i in enumerate(intervals):
		if is_overlap(i, new_interval) and not start:
			kill.append(idx)
			start = True
		elif not is_overlap(i, new_interval) and start and not finish:
			kill.append(idx - 1)
			finish = True
			break
	if len(kill) == 1:
		kill.append(len(intervals) - 1)
	elif len(kill) == 0:
		for idx, i in enumerate(intervals):
			if new_interval[1] < i[0]:
				intervals.insert(idx, new_interval)
				return intervals
		intervals.append(new_interval)
		return intervals
	new_one = [min(intervals[kill[0]][0], new_interval[0]), 
		   max(intervals[kill[1]][1], new_interval[1])]
	for i in range(kill[0], kill[1] + 1):
		del intervals[kill[0]]
	intervals.insert(kill[0], new_one)
	
	return intervals

print(insert(intervals, new_interval))

			



	
		
		

