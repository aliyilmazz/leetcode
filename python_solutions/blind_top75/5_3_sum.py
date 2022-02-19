# class Triplet:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#         self.triplet_list = sorted(list((a, b, c)))
#
#     def __hash__(self):
#         return self.triplet_list[0] * 100 + self.triplet_list[1] * 10 + self.triplet_list[2]
#
#     def __repr__(self):
#         return "Triplet(%s, %s, %s)" % (self.a, self.b, self.c)
#
#     def __eq__(self, other):
#         return other.triplet_list == self.triplet_list
#
#     # def __ne__(self, other):
#     #     return not self.__eq__(other)
#

class Solution(object):

    def twoSum(self, nums, target):
        left_index, right_index = 0, len(nums)-1
        while left_index < right_index:
            sum = nums[left_index] + nums[right_index]
            if sum > target:
                while right_index > left_index and nums[right_index-1] == nums[right_index]:
                    right_index -= 1
                right_index -= 1
            elif sum < target:
                while left_index < right_index and nums[left_index+1] == nums[left_index]:
                    left_index += 1
                left_index += 1
            else:
                #self.triplets.add(Triplet(target*-1, nums[left_index], nums[right_index]))
                self.triplets.append([target*-1, nums[left_index], nums[right_index]])
                while left_index < right_index and nums[left_index+1] == nums[left_index]:
                    left_index += 1
                left_index += 1
                while right_index > left_index and nums[right_index-1] == nums[right_index]:
                    right_index -= 1
                right_index -= 1


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        
        sort nums
        starting from leftmost, set target and find target in array remaining in right side.
             * apply two pointers to right indices 
        '''

        self.triplets = []
        nums.sort()

        #print(nums)
        for _index, num in enumerate(nums):
            #print("Index:%s, target:%s" % (_index, num*-1))
            if _index > 0 and nums[_index-1] == nums[_index]:
                continue
            self.twoSum(nums[_index+1:len(nums)], target=num*-1)


        return self.triplets



if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    triplets = Solution().threeSum(nums)
    print("Nums:%s, Triplets:%s" % (nums, triplets))

    nums = []
    triplets = Solution().threeSum(nums)
    print("Nums:%s, Triplets:%s" % (nums, triplets))

    nums = [0]
    triplets = Solution().threeSum(nums)
    print("Nums:%s, Triplets:%s" % (nums, triplets))