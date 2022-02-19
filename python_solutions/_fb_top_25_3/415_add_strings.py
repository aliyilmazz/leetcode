class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        str to integer
        ignore trailing whitespace
        check sign character if exists
        read digits, ignore rest
        if no digits read, return 0
        clamp result into integer ranges
        '''

        s = s.strip()
        sign = {'+', '-'}
        sign_found = 0

        if not s:
            return 0

        if s[0] in sign:
            sign_found = -1 if s[0] == '-' else 1
            s = s[1:]

        digits = ''

        for char in s:
            if not char.isdigit():
                break
            digits += char

        if not digits:
            return 0

        num = int(digits)
        if sign_found != 0:
            num *= sign_found

        num = min(2 ** 31 - 1, num)
        num = max(-2 ** 31, num)
        return num

