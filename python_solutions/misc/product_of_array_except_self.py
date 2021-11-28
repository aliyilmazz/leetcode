from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        * traverse from left to right, populate array
        * traverse from right to left, multiply populated array
        """

        lefts = []
        sum = 1
        for _index, num in enumerate(nums):
            lefts.append(sum)
            sum *= num

        # right_cumulative_sum = 1
        # _index = len(nums)-1
        # for num in nums[::-1]:
        #     right_cumulative_sum *= num
        #     if _index != 0:
        #         lefts[_index-1] *= right_cumulative_sum
        #     _index -= 1

        sum = 1
        for _index in range(len(nums)-1, -1, -1):
            lefts[_index] *= sum
            sum *= nums[_index]

        return lefts


def test_case(input, expected_output):
    output = Solution().productExceptSelf(input)
    try:
        assert output == expected_output
    except AssertionError:
        print("---\nError!\nInput\t\t: %s\nExpected\t: %s\nActual\t\t: %s\n---" % (input, expected_output, output))


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    output = Solution().productExceptSelf(nums)
    print("Input: %s\nOutput: %s" % (nums, output))

    test_case(
        input=[1, 2, 3, 4],
        expected_output=[24, 12, 8, 6]
    )

    test_case(
        input=[-1, 1, 0, -3, 3],
        expected_output=[0, 0, 9, 0, 0]
    )