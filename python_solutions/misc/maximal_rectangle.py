from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        if len(set(timePoints)) > len(timePoints):
            return 0

        time_points = [[int(x) for x in tp.split(":")] for tp in timePoints]
        normalize = lambda x: x[0] * 60 + x[1]
        normalized_time_points = list(set([normalize(x) for x in time_points]))

        minimum = 999999
        maximum = 0
        for i in range(len(normalized_time_points)):
            for j in range(i+1, len(normalized_time_points)):
                difference = abs(normalized_time_points[i] - normalized_time_points[j])
                minimum = min(minimum, difference)
                maximum = max(maximum, difference)

        MINUTES_IN_DAY = 1440

        alternative_minimum = MINUTES_IN_DAY - maximum
        minimum = min(alternative_minimum, minimum)
        return minimum


if __name__ == '__main__':
    timePoints = ["00:00","23:59","00:00"]
    print("min diff: %s" % Solution().findMinDifference(timePoints))