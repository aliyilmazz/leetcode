class Solution:
    def isNumber(self, s: str) -> bool:

        # both decimal numbers and integers must contain at least one digit
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

        # optional. if it will be present, it better be first char. else, return false
        signs = {'+', '-'}

        # optional. if it's present, it should be followed by a number
        exponents = {'E', 'e'}

        DOT = '.'


        seen_digit, seen_exponent, seen_dot = False, False, False

        for i, c in enumerate(s):

            if c in signs and i>0 and s[i-1] not in exponents:
                return False  # invalid sign trap

            if c in exponents and (seen_exponent or not seen_digit):
                return False  # invalid exponent trap

            if c == DOT and (seen_dot or seen_exponent):
                return False  # invalid DOT trap

            if c in digits:
                seen_digit = True  # set flag for future checks
            elif c in exponents:
                seen_exponent = True
                seen_digit = False
            elif c == DOT:
                seen_dot = True
            elif c in signs:
                pass  # we did sign trap before. noop
            else:
                return False

        return seen_digit


if __name__ == '__main__':
    num = "0"
    output = Solution().isNumber(num)
    print("num: %s, output: %s" % (num, output))