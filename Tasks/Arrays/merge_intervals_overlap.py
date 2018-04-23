class Interval:
	def __init__(self, s = 0, e = 0):
		self.start = s
		self.end = e

class Solution:
	def sort_by_x(self, interval):
		return interval.start

	def is_overlap(self, first, second):
		if max(first.start, second.start) <= min(first.end, second.end):
			return True
		else:
			return False
	
	def merge(self, intervals):
		intervals.sort(key = self.sort_by_x)
		ans = []
		if len(intervals) == 0:
			return []
		current = intervals[0]
		for i in range(1, len(intervals)):
			if self.is_overlap(current, intervals[i]):
				current = Interval(current.start, max(intervals[i].end, current.end))
			else:
				ans.append(current)
				current = intervals[i]
		ans.append(current)
		return ans

sol = Solution()
int1 = Interval(1, 10)
int2 = Interval(2, 9)
int3 = Interval(6, 10)
int4 = Interval(10, 18)
ans = sol.merge([])
for interval in ans:
	print(interval.start, interval.end)