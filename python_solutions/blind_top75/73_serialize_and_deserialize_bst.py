class Solution:
    def eraseOverlapIntervals_soln1(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        if not n:
            return 0

        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            max_value = 0
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    max_value = max(max_value, dp[j])
                dp[i] = max_value + 1

        non_overlapping_intervals = max(dp)
        return n - non_overlapping_intervals

    def eraseOverlapIntervals_dptwo(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        if not n:
            return 0

        intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            max_value = 0
            for j in range(i - 1, -1, -1):
                if intervals[j][1] <= intervals[i][0]:
                    max_value = max(max_value, dp[j])
                    break
            dp[i] = max(max_value + 1, dp[i - 1])

        non_overlapping_intervals = max(dp)
        return n - non_overlapping_intervals

    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        n = len(intervals)

        count = 0
        prev = intervals[0]
        for i in range(1, n):
            interval = intervals[i]
            if interval[0] >= prev[1]:
                prev = interval
                continue
            else:
                # there is an overlapping
                if interval[1] < prev[1]:
                    prev = interval  # replace last one with current one 
                count += 1
        return count
