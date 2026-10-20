class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        ani = 0
        count = 1
        for i in range(1,n):
            if intervals[i][0] >= intervals[ani][1]:
                count +=1
                ani = i

        return n - count    

        