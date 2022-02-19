class Solution:
    def findPeakElement_tle(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i

        return len(nums) - 1

    def findPeakElement_iterative_bs(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left

    def findPeakElement(self, nums: List[int]) -> int:

        def _binarySearch(nums, left, right):
            if left == right:
                return left

            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                return _binarySearch(nums, mid + 1, right)
            else:
                return _binarySearch(nums, left, mid)

        return _binarySearch(nums, 0, len(nums) - 1)