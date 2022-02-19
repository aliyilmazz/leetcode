from typing import List

class Solution:

    def _search_in_sorted_array(self, nums, start, end, target):
        #print("start: %s, end:%s" % (start, end))
        if start > end:
            return -1

        if start == end:
            return start if nums[start] == target else -1

        middle = (start + end) // 2
        mid_num = nums[middle]

        if target <= mid_num:
            return self._search_in_sorted_array(nums, start, middle, target)
        else:
            return self._search_in_sorted_array(nums, middle + 1, end, target)


    def _search(self, nums, start, end, target):
        #print("start: %s, end: %s" % (start, end))

        if start > end:
            return -1

        if start == end:
            return start if nums[start] == target else -1

        middle = (start + end) // 2

        start_num = nums[start]
        mid_num = nums[middle]
        end_num = nums[end]

        if start_num <= mid_num:  # left side is sorted
            if start_num <= target <= mid_num:  # remains in left side
                return self._search_in_sorted_array(nums, start, middle, target)
            else:  # left is sorted but number remains in right side
                return self._search(nums, middle + 1, end, target)
        else:  # right side is sorted
            if mid_num < target <= end_num:  # and my target remains in right side
                return self._search_in_sorted_array(nums, middle+1, end, target)
            else:
                # and my target remains in unsorted left side
                return self._search(nums, start, middle, target)

    def search_recursive(self, nums: List[int], target: int) -> int:
        '''
        recursively apply BST to narrowed down indices
        '''
        return self._search(nums, 0, len(nums) - 1, target)

    def search(self, nums, target):

        start, end = 0, len(nums)-1


        while start <= end:

            # if start == end:
            #     return start if nums[start] == target else -1

            middle = (start+end) // 2
            start_num = nums[start]
            end_num = nums[end]
            middle_num = nums[middle]

            if target == middle_num:
                return middle

            if start_num <= middle_num:  # left side is sorted...
                if start_num <= target < middle_num:  # ...and our target is at left side
                    end = middle
                    continue
                else:  # ...and our target is in unsorted right side
                    start = middle+1
                    continue
            else:  # leftside is not sorted AKA right side is sorted
                if middle_num < target <= end_num:  # target is at sorted right side
                    start = middle + 1
                    continue
                else:  # our target is at unsorted left side
                    end = middle

        return -1








if __name__ == '__main__':
    nums = [1, 2, 3, 5]
    index = Solution().search(nums, target=2)
    print("index: %s" % index)