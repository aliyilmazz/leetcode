from typing import List


class Solution:

    @staticmethod
    def deserialize(digits):
        number = 0
        multiplier = 1
        for digit in reversed(digits):
            number += multiplier * digit
            multiplier *= 10
        return number

    @staticmethod
    def serialize(number) -> List[int]:
        biggest_multiplier = 1
        while biggest_multiplier * 10 <= number:
            biggest_multiplier *= 10

        digits = []

        while True:
            if number == 0:
                digit = 0
            else:
                digit = int(number / biggest_multiplier)
            digits.append(digit)
            number -= digit * biggest_multiplier
            if biggest_multiplier == 1:
                break
            else:
                biggest_multiplier //= 10

        return digits

    def plusOne(self, digits: List[int]) -> List[int]:
        return self.serialize(self.deserialize(digits) + 1)


def verboseAssert(_list):
    output = Solution().plusOne(_list)
    print("Input:  %s\nOutput: %s" % (_list, output))


if __name__ == '__main__':
    verboseAssert([1, 2, 3])
    verboseAssert([9, 9])
    verboseAssert([0])
    verboseAssert([9])
    verboseAssert([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3])

    assert (Solution().plusOne([1, 2, 3]) == [1, 2, 4])
    assert (Solution().plusOne([9, 9]) == [1, 0, 0])
    assert (Solution().plusOne([0]) == [1])
    assert (Solution().plusOne([9]) == [1, 0])
    assert (Solution().plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]) == [6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 4])

    print("all done!")
