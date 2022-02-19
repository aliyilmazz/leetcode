from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        return [[]]



if __name__ == '__main__':
    points = [[2, 2], [1, 3]]
    k = 1
    output = Solution().kClosest(points, k)
    print("Points: %s, k: %s\nOutput: %s\n\n" % (points, k, output))