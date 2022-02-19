class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.nonzero_indexes = dict()
        for _index, num in enumerate(nums):
            if num:
                self.nonzero_indexes[_index] = num


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        self_set = self.nonzero_indexes.keys()
        opposing_set = vec.nonzero_indexes.keys()

        intersection_set = self_set & opposing_set

        sum = 0
        for common_index in intersection_set:
            sum += vec.nonzero_indexes[common_index] * self.nonzero_indexes[common_index]

        return sum








# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)



if __name__ == '__main__':
    nums1 = [1, 0, 0, 2, 3]
    nums2 = [0, 3, 0, 4, 0]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    ans = v1.dotProduct(v2)
    print("Nums1: %s\nNums2: %s\nAnswer: %s" % (nums1, nums2, ans))


    nums1 = [0, 1, 0, 0, 2, 0, 0]
    nums2 = [1, 0, 0, 0, 3, 0, 4]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    ans = v1.dotProduct(v2)
    print("Nums1: %s\nNums2: %s\nAnswer: %s" % (nums1, nums2, ans))