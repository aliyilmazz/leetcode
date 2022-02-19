from typing import List
import random


class Solution:

    def partition(self, nums, left, right):
        if left == right:
            return nums[left]

        pivot_index = random.randint(left, right)  # both inclusive

        pivot = nums[pivot_index]

        # move pivot to right
        nums[right], nums[pivot_index] = nums[pivot_index], nums[right]

        # start iterating each element
        smaller_array_offset = left  # increment this for each smaller item faced
        for i in range(left, right):  # dont include right, because `n.right` is pivot
            if nums[i] < pivot:
                nums[smaller_array_offset], nums[i] = nums[i], nums[smaller_array_offset]
                smaller_array_offset += 1

        # at the end of iteration, if 3 items are placed at left, our offset is 3
        # put pivot back in position
        nums[smaller_array_offset], nums[right] = nums[right], nums[smaller_array_offset]
        return smaller_array_offset

    def select_random_index(self, nums, left, right, k):
        #print("partitioning...")
        #print("nums: %s" % nums)
        random_index = self.partition(nums, left, right)
        #print("random index: %s" % random_index)
        #print("nums: %s" % nums)
        #print("left: %s" % left)
        #print("right: %s" % right)
        if random_index == k:
            return nums[random_index]
        elif random_index > k:  # process smaller array (in left)
            return self.select_random_index(nums, left, random_index - 1, k)
        else:  # process larger array (in right)
            return self.select_random_index(nums, random_index + 1, right, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.select_random_index(nums, 0, len(nums) - 1, len(nums) - k)



if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    output = Solution().findKthLargest(nums, k)
    print("nums: %s\nk:%s\nOutput:%s" % (nums, k, output))