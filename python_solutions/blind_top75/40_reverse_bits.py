from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        '''

        a------b------c

        a<b<c

        a------b------c

        9012345678
        4  8  3
        9 3 8

        90123
        n=5
        m=2

        901
        n=3
        m=1


        behavior: always head to unsorted arr
        basecase:
        if n==2, return min(a,b)
        '''

        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            # print("l:%s, r:%s" % (left,right))
            if left == right - 1:
                return min(nums[left], nums[right])

            middle = (left + right) // 2
            left_num, middle_num, right_num = nums[left], nums[middle], nums[right]

            if left_num < middle_num < right_num:
                # properly sorted
                return left_num

            if left_num < middle_num:
                # left side is sorted
                # action: go for right side
                left = middle + 1
                continue
            else:
                # right side is sorted
                #  action: go for left
                right = middle
                continue

        return nums[left]


if __name__ == '__main__':
    output = Solution().findMin([3,4,5,1,2])
    print("output: %s" % output)