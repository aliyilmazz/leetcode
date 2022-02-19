from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        initial_interval = intervals[0]
        start = initial_interval[0]
        end = initial_interval[1]

        merged_intervals = []

        for interval in intervals[1:]:
            next_start = interval[0]
            next_end = interval[1]
            if end >= next_start:
                end = max(end, next_end)
            else:
                merged_intervals.append([start, end])
                start = next_start
                end = next_end

        merged_intervals.append([start, end])
        return merged_intervals


if __name__ == '__main__':
    pass
    #Solution().merge()