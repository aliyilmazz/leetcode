from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero_runner = 0

        global_runner = 0
        while global_runner < len(nums):
            current_number = nums[global_runner]
            if current_number == 0:
                global_runner += 1
                continue
            else:
                if global_runner > nonzero_runner:
                    nums[nonzero_runner] = nums[global_runner]
                    nums[global_runner] = 0
                    nonzero_runner += 1
                    global_runner += 1
                    continue
                else:
                    nonzero_runner += 1
                    global_runner += 1
        return nums


def verboseAssert(_list):
    output = Solution().moveZeroes(_list)
    print("Input:  %s\nOutput: %s" % (_list, output))


if __name__ == '__main__':
    verboseAssert([0, 1, 0, 3, 12])
    verboseAssert([0])
