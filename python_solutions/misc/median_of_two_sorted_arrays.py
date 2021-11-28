from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        while nums1 or nums2:
            if nums1 and nums2:
                if nums1[0] <= nums2[0]:
                    nums.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    nums.append(nums2[0])
                    nums2 = nums2[1:]
            else:
                if not nums2:
                    nums.append(nums1[0])
                    nums1 = nums1[1:]
                elif not nums1:
                    nums.append(nums2[0])
                    nums2 = nums2[1:]

        print("nums:%s" % nums)
        if len(nums) % 2 == 0:
            return (nums[len(nums)//2] + nums[(len(nums)//2)-1]) / 2
        else:
            return nums[len(nums)//2]


if __name__ == '__main__':
    # nums1 = [1, 3]
    # nums2 = [2]
    # print("Inputs:%s %s, Output: %s" % (nums1, nums2, Solution().findMedianSortedArrays(nums1, nums2)))

    nums1 = [1,2]
    nums2 = [3,4]
    print("Inputs:%s %s, Output: %s" % (nums1, nums2, Solution().findMedianSortedArrays(nums1, nums2)))

    # nums1 = [1, 3]
    # nums2 = [2]
    # print("Inputs:%s %s, Output: %s" % (nums1, nums2, Solution().findMedianSortedArrays(nums1, nums2)))
    #
    # nums1 = [1, 3]
    # nums2 = [2]
    # print("Inputs:%s %s, Output: %s" % (nums1, nums2, Solution().findMedianSortedArrays(nums1, nums2)))
