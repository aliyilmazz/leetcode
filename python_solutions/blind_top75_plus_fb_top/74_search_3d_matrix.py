from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0

        left_max = [0] * n
        left_max[0] = height[0]

        right_max = [0] * n
        right_max[n-1] = height[n-1]

        for i in range(n-1):
            left_max[i] = max(height[i], left_max[i-1])

        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])

        for i in range(n):
            water = min(left_max[i], right_max[i]) - height[i]
            total_water += max(water, 0)

        return total_water


if __name__ == '__main__':
    output = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print("output: %s" % output)