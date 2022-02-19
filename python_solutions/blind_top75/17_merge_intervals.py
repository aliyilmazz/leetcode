from typing import List


class Solution:
    def canJump_backtrack(self, nums: List[int]) -> bool:
        '''
        very inefficient. o(2^n) time. o(n) space
        '''
        if not nums:
            return False

        if len(nums) == 1:
            return True

        return any([self.canJump(nums[i:]) for i in range(nums[0], 0, -1)])

    def canJump_dp(self, nums):
        '''
        top to bottom DP, o(n2) time, o(n) space due to DP array
        '''
        n = len(nums)
        dp = [0] * n
        dp[n - 1] = 1  #  last element

        for _index in range(n - 2, -1, -1):
            step_capacity = nums[_index]
            step_capacity = min(n - 1, step_capacity + _index)  #  clamp for array
            for step in range(step_capacity, _index, -1):
                if dp[step] == 1:
                    dp[_index] = 1  # mark as good
                    break
            else:
                dp[_index] = 2  #  mark as bad

        if dp[0] == 1:
            return True

        return False

    def canJump(self, nums):
        ''' try to update leftmost index as we go '''
        ''' o(1) space, o(n) time '''
        n = len(nums)
        leftmost_index = n - 1

        for _index in range(n - 1, -1, -1):
            if nums[_index] + _index >= leftmost_index:
                leftmost_index = _index

        return leftmost_index == 0



if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]
    result = Solution().canJump(nums)
    print("nums: %s, result: %s" % (nums, result))