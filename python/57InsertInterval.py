#merge interval but add another interval in first
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        rv = list()
        rv.append(intervals[0])
        for i in intervals:
            if i[0] <= rv[-1][1]:
                rv[-1][1] = max(rv[-1][1],i[1])
            else:
                rv.append(i)
        return rv