class Solution(object):

    @staticmethod
    def calculateMaxArea(height, left_index, right_index):
        return (right_index - left_index) * min(height[left_index], height[right_index])

    def shiftLeft(self):
        for new_left_candidate in range(self.left_index, self.right_index):
            if self.height[new_left_candidate] > self.height[self.left_index]:
                new_max_area = Solution.calculateMaxArea(self.height, new_left_candidate, self.right_index)
                self.max_area = max(self.max_area, new_max_area)
                self.left_index = new_left_candidate
                print("shifted left! new leftindex: %s, new score: %s" % (self.left_index, self.max_area))
                return True

        return False

    def shiftRight(self):
        for new_right_candidate in range(self.right_index, self.left_index, -1):
            if self.height[new_right_candidate] > self.height[self.right_index]:
                new_max_area = Solution.calculateMaxArea(self.height, self.left_index, new_right_candidate)
                self.max_area = max(self.max_area, new_max_area)
                self.right_index = new_right_candidate
                print("shifted right! new right_index: %s, new score: %s" % (self.right_index, self.max_area))
                return True
        return False

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        ''' 
            outline left, right pointers
            one by one, shift left, shift right, until you cant shift right and shift left
        '''

        self.height = height
        self.left_index, self.right_index = 0, len(height)-1

        self.max_area = Solution.calculateMaxArea(self.height, self.left_index, self.right_index)

        while True:
            shift_operation = self.shiftLeft \
                if self.height[self.left_index] < self.height[self.right_index] \
                else self.shiftRight

            shifted = shift_operation()
            if not shifted:
                break

        return self.max_area

if __name__ == '__main__':
    # height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # print("Height:%s, Output:%s" % (height, Solution().maxArea(height)))
    #
    # height = [4,3,2,1,4]
    # print("Height:%s, Output:%s" % (height, Solution().maxArea(height)))
    #
    # height = [1, 2, 1]
    # print("Height:%s, Output:%s" % (height, Solution().maxArea(height)))

    height = [2,3,4,5,18,17,6]
    print("Height:%s, Output:%s" % (height, Solution().maxArea(height)))



