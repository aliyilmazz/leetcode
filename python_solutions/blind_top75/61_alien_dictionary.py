class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        return next(iter(set(range(n)) - set(nums)))