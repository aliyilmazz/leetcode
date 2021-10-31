from typing import List


class Solution:

    def rotate(self, input: List[List[int]]) -> None:

        n = len(input)


        lower_bound = 0
        upper_bound = n-1
        while lower_bound < upper_bound:
            for i in range(upper_bound-lower_bound):
                temp = input[lower_bound][lower_bound+i]
                input[lower_bound][lower_bound + i] = input[upper_bound - i][lower_bound]
                input[upper_bound - i][lower_bound] = input[upper_bound][upper_bound - i]
                input[upper_bound][upper_bound - i] = input[lower_bound+i][upper_bound]
                input[lower_bound + i][upper_bound] = temp
            lower_bound += 1
            upper_bound -= 1
        #input = [list(a) for a in zip(*reversed(input))]


def verbose_assert(_list):
    print("List(before): %s" % _list)
    Solution().rotate(_list)
    print("List(after):  %s" % _list)


if __name__ == '__main__':
    input = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    verbose_assert(input)


"""
input = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

output = [
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
]


input2 = [
    [1, 2],
    [3, 4]
]

output2 = [
    [3, 1],
    [4, 2]
]

0,0(temp) <- 1,0 <- 1,1 <- 0,1 <- temp


0,0(temp) <- 3,0 <- 3,3 <- 0,3 <- temp
0,1(temp) <- 2,0 <- 3,2 <- 1,3 <- temp
0,1(temp) <- 2,0 <- 3,2 <- 1,3 <- temp
"""