class Solution:

    def numDecodings(self, s: str) -> int:

        '''
        letter_map = {
            '1': 'A',
            '2': 'B',
            '3': 'C',
            '4': 'D',
            '5': 'E',
            '6': 'F',
            '7': 'G',
            '8': 'H',
            '9': 'I',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
            '10': 'J',
        }
        '''

        if s == '' or s.startswith('0'):
            return 0

        if len(s) == 1:
            return 1

        if int(s) in [10, 20]:
            return 1

        if len(s) == 2 and 10 <= int(s) <= 26:
            return 2

        single_digit = s[0]
        double_digit = s[0:2]

        count = 0
        if single_digit != '0':
            count += self.numDecodings(s[1:])
        if 10 <= int(double_digit) <= 26:
            count += self.numDecodings(s[2:])

        return count


if __name__ == '__main__':
    num = "10"
    output = Solution().numDecodings(num)
    print("num: %s, output: %s" % (num, output))
