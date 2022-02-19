class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left_index, right_index = 0, len(numbers)-1
        while left_index < right_index:
            sum = numbers[left_index] + numbers[right_index]
            if sum > target:
                right_index -= 1
            elif sum < target:
                left_index += 1
            else:
                return [left_index+1, right_index+1]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    output = Solution().twoSum(numbers, target)
    print("Output: %s" % output)