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

    def insert_prevclone(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ''' insert and merge '''
        intervals.append(newInterval)
        return self.merge(intervals)

    def insert(self, intervals, newInterval):

        new_start, new_end = newInterval
        n = len(intervals)

        results = []

        # add previous ones
        interval_index = 0
        while interval_index < n and intervals[interval_index][0] < new_start:
            results.append(intervals[interval_index])
            interval_index += 1

        # insert interval
        if not results or results[-1][1] < new_start:
            results.append([new_start, new_end])
        else:
            results[-1][1] = max(results[-1][1], new_end)

        # add remaining intervals, merge if needed

        _, curr_end = results[-1]
        while interval_index < n:
            next_start, next_end = intervals[interval_index]
            if next_start > curr_end:
                results.append(intervals[interval_index])
                curr_end = next_end
            else:
                results[-1][1] = max(next_end, curr_end)
                curr_end = max(next_end, curr_end)

        return results









if __name__ == '__main__':
    pass
    #Solution().merge()