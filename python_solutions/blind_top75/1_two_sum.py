class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complementary_map = {}
        for _index, num in enumerate(nums):
            complementary = target - num
            if complementary in complementary_map:
                first_index = complementary_map[complementary]
                second_index = _index
                return [first_index, second_index]
            else:
                # register this number for incoming lookups
                complementary_map[num] = _index


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    print("%s" % Solution().twoSum(nums, target))