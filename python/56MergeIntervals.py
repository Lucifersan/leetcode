class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        rv = list()
        rv.append(intervals[0])
        for i in intervals:
            if i[0] <= rv[-1][1]:
                rv[-1][1] = max(rv[-1][1],i[1])
            else:
                rv.append(i)
        return rv
        