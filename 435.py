class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: (x[0], x[1]))
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                count += 1
                intervals[i + 1][1] = min(intervals[i][1], intervals[i + 1][1])

        return count
