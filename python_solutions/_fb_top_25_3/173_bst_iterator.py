from collections import deque


class Solution:

    def isGreater(self, num1, num2):
        if len(num1) != len(num2):
            return len(num1) > len(num2)

        if num1[0] != num2[0]:
            return num1[0] > num2[0]

        return self.isGreater(num1[1:], num2[1:])

    def add(self, num1: str, num2: str) -> str:

        N1, N2 = len(num1), len(num2)

        n1, n2 = N1 - 1, N2 - 1

        result = deque()
        sum, carry = 0, 0

        while n1 >= 0 or n2 >= 0 or carry:
            digit1, digit2 = 0, 0
            if n1 >= 0:
                digit1 = ord(num1[n1]) - ord('0')
                n1 -= 1

            if n2 >= 0:
                digit2 = ord(num2[n2]) - ord('0')
                n2 -= 1

            sum = digit1 + digit2 + carry
            carry = sum // 10
            sum %= 10

            result.appendleft(sum)

        return ''.join([str(digit) for digit in result])

    def subtract(self, num1, num2):

        N1, N2 = len(num1), len(num2)
        n1, n2 = N1 - 1, N2 - 1

        result = deque()
        sub, borrow = 0, 0

        while n1 >= 0 or n2 >= 0:
            digit1, digit2 = ord(num1[n1]) - ord('0'), 0

            if n2 >= 0:
                digit2 = ord(num2[n2]) - ord('0')
                n2 -= 1

            sub = digit1 - digit2 - borrow
            if sub < 0:
                sub += 10
                borrow = 1

            result.appendleft(sub)
            n1 -= 1

        return ''.join([str(digit) for digit in result])

    def addStrings(self, num1: str, num2: str) -> str:

        if num1[0] == '-' and num2[0] == '-':
            return '-' + self.add(num1[1:], num2[1:])

        if num1[0] == '-' and num2[0] != '-':
            if self.isGreater(num1[1:], num2):
                return '-' + self.subtract(num1[1:], num2)
            else:
                return self.subtract(num2, num1[1:])

        if num1[0] != '-' and num2[0] == '-':
            if self.isGreater(num2[1:], num1):
                return '-' + self.subtract(num2[1:], num1)
            else:
                return self.subtract(num1, num2[1:])

        else:
            return self.add(num1, num2)




if __name__ == '__main__':

    Solution().subtract("150", "140")


    num1, num2 = "120", "130"
    print("%s + %s = %s" % (num1, num2, Solution().addStrings(num1, num2)))

    num1, num2 = "120", "-130"
    print("%s + %s = %s" % (num1, num2, Solution().addStrings(num1, num2)))

    num1, num2 = "-120", "130"
    print("%s + %s = %s" % (num1, num2, Solution().addStrings(num1, num2)))

    num1, num2 = "-120", "-130"
    print("%s + %s = %s" % (num1, num2, Solution().addStrings(num1, num2)))
