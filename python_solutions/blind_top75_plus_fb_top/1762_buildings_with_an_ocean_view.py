class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """

        ''' 

            * iterate from right to left
            * for _index in range(len(buildings)-1, -1, -1):
                building = buildings[_index]
                * if building is above threshold, 
                    * add to list of ocean-view buildings
                    * update threshold




        '''

        indices = []

        # todo: iterate and populate indices

        minimum_required_height = 0
        for _index in range(len(heights) - 1, -1, -1):
            building_height = heights[_index]
            if building_height > minimum_required_height:
                indices.append(_index)
                minimum_required_height = building_height
            else:
                pass

        return list(reversed(indices))


if __name__ == '__main__':
    heights = [4, 2, 3, 1]
    output = Solution().findBuildings(heights)
    print("Input: %s\nOutput: %s" % (heights, output))

    heights = [4, 3, 2, 1]
    output = Solution().findBuildings(heights)
    print("Input: %s\nOutput: %s" % (heights, output))

    heights = [2, 2, 2, 2]
    output = Solution().findBuildings(heights)
    print("Input: %s\nOutput: %s" % (heights, output))


