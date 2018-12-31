from itertools import combinations



class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_set = set(nums)
        for num_index, num in enumerate(nums):
            print("target-num: " + str(target-num))
            if (target-num) in num_set:
                first_index = num_index
                if num == target-num:
                    try:
                        second_index = nums[first_index+1:].index(target-num)+first_index+1
                    except Exception as e:
                        continue
                else:
                    second_index = nums.index(target-num)
                return [first_index, second_index]


sol = Solution()
indices = sol.twoSum([3,2,4], 6)
print(str(indices))
