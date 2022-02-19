class Solution:
    def merge_omspace(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_copy = nums1[:m]

        p1, p2 = 0, 0

        # compare elements from nums1copy&nums2, write smallest so nums1
        for i in range(m + n):
            if p1 >= m or p2 >= n:
                if p1 >= m:
                    nums1[i] = nums2[p2]
                    p2 += 1
                    continue
                if p2 >= n:
                    nums1[i] = nums1_copy[p1]
                    p1 += 1
                    continue

            if nums1_copy[p1] <= nums2[p2]:
                nums1[i] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1

    def merge_o1space(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        p1, p2 = m - 1, n - 1

        # move i backwards through the array(num1)
        # each time, write biggest value pointed at p1|p2

        for i in range(m + n - 1, -1, -1):
            if p2 < 0:
                break

            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        p1, p2 = m - 1, n - 1

        for p in range(m + n - 1, -1, -1):

            cand1 = nums1[p1] if p1 > -1 else float('-inf')
            cand2 = nums2[p2] if p2 > -1 else float('-inf')

            if cand2 >= cand1:
                nums1[p] = cand2
                p2 -= 1
            else:
                nums1[p] = cand1
                p1 -= 1








