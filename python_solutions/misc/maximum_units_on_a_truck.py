from typing import List
import unittest

class Solution:

    def _fetch_box(self):
        #print("#sortedboxtypes before fetch:%s" % self.sorted_box_types)

        if not self.sorted_box_types:
            return -1

        biggest_box_type = self.sorted_box_types[0]
        box_count, box_type = biggest_box_type

        self.sorted_box_types[0][0] -= 1
        if self.sorted_box_types[0][0] == 0:
            self.sorted_box_types = self.sorted_box_types[1:]

        #print("#sortedboxtypes after fetch:%s" % self.sorted_box_types)

        return box_type

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        :param boxTypes: boxes and their sizes
        :param truckSize: total box capacity of truck
        :return: number of boxes that can be loaded into the truck
        """

        """
            put them into a priority queue, pop each box from queue until you reach trucksize.
        """
        self.sorted_box_types = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        total_unit = 0

        for _ in range(truckSize):
            added_unit = self._fetch_box()
            if added_unit == -1:
                return total_unit
            total_unit += added_unit
            #print("score after fetch:%s" % total_unit)

        return total_unit







def test_case(**kwargs):
    output = Solution().maximumUnits(**{k: v for k,v in kwargs.items() if k!='expected_output'})
    try:
        assert output == kwargs['expected_output']
    except AssertionError:
        print("##expected:%s,\nactual:%s" % (kwargs['expected_output'], output))


if __name__ == '__main__':
    test_case(boxTypes=[[1,3], [2,2], [3,1]], truckSize=4, expected_output=8)
    test_case(boxTypes=[[5,10],[2,5],[4,7],[3,9]], truckSize=10, expected_output=91)