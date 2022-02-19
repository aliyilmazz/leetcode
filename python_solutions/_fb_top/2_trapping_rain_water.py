from typing import List


class Solution:
    def merge(self, nums, left, mid, right):

        ptr1 = left
        ptr2 = mid + 1
        while ptr1 <= mid and ptr2 <= right:
            if nums[ptr1] <= nums[ptr2]:
                ptr1 += 1
                continue

            temp = nums[ptr2]
            ptr2_traverser = ptr2
            # shift all elements between element1 and element2, right by 1
            while ptr2_traverser != ptr1:
                nums[ptr2_traverser] = nums[ptr2_traverser - 1]
                ptr2_traverser -= 1
            nums[ptr1] = temp

            ptr1 += 1
            ptr2 += 1
            mid += 1

    def merge_sort(self, nums, left, right):

        if left == right:
            return

        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)

        self.merge(nums, left, mid, right)

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return None

        n = len(nums)
        prev_index = n - 1

        for i in range(n - 2, -1, -1):
            if nums[prev_index] > nums[i]:
                smaller_greatest_index = prev_index
                for j in range(i + 1, n):
                    if nums[j] < nums[smaller_greatest_index] and nums[j] > nums[i]:
                        smaller_greatest_index = j

                nums[i], nums[smaller_greatest_index] = nums[smaller_greatest_index], nums[i]
                # print("nums before ms: %s" % nums)
                self.merge_sort(nums, i + 1, n - 1)
                return
            prev_index = i
        else:
            # reverse entire number
            left, right = 0, n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return


if __name__ == '__main__':
    nums = [3, 2, 1]
    output = Solution().nextPermutation(nums)
    print("output: %s" % output)