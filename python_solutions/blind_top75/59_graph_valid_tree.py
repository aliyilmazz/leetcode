class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)

        if n < 2:
            return True

        intervals.sort(key=lambda x: x[0])

        prev_end = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] < prev_end:
                return False
            prev_end = intervals[i][1]

        return True
