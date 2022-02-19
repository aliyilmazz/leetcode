import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        '''
        self.interval_size = sum(w)
        self.upper_bound_list = [0]
        upper_bound = 0
        for _index, element in enumerate(w):
            # calculate and register upper bound for each index
            upper_bound += element
            self.upper_bound_list.append(upper_bound)
        '''


        self.upper_bound_list = []
        upper_bound = 0
        for _index, element in enumerate(w):
            # calculate and register upper bound for each index
            upper_bound += element
            self.upper_bound_list.append(upper_bound)
        self.interval_size = upper_bound

    def pickIndex(self) -> int:


        '''
        pick left, right = 0, len-1
        while left != right-1:
            mid = (left+(right-left)) // 2
            if random<mid:
                right = mid-1
            else if random > mid:
                left = mid+1
        '''

        random_number_within_interval = 1.111
        #random_number_within_interval = random.uniform(0, self.interval_size)
        left, right = 0, len(self.upper_bound_list)-1
        while left < right:  # loop until left and right gets next to each other.
            mid_index = int((left + (right-left)) // 2)
            mid = self.upper_bound_list[mid_index]

            if mid == random_number_within_interval:  # if mid is equal, then this is right index
                return mid_index

            else:
                if mid > random_number_within_interval:  # if mid is larger, take left side
                    right = mid_index
                else:  # if mid is smaller, take right side into account
                    left = mid_index + 1

        return left




if __name__ == '__main__':
    output = Solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]).pickIndex()
    print("output: %s" % output)

