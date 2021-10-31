from typing import List


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        reading_digit = False
        reading_sign = False
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        signs = {'+', '-'}
        recorded_characters = []
        while i < len(s):
            if reading_sign:
                if s[i] in signs:
                    return 0
                elif s[i] in digits:
                    recorded_characters.append(s[i])
                    i += 1
                    reading_sign = False
                    reading_digit = True
                else:
                    # unrecognized character after sign
                    return 0

            elif reading_digit:
                if s[i] not in digits:
                    break
                else:
                    recorded_characters.append(s[i])
                    i += 1

            else:
                # not started reading characters yet.
                if s[i] == ' ':
                    # skip leading whitespace
                    i += 1

                elif s[i] in digits:
                    reading_digit = True
                    recorded_characters.append(s[i])
                    i += 1

                elif s[i] in signs:
                    reading_sign = True
                    recorded_characters.append(s[i])
                    i += 1

                else:
                    return 0
        resulting_int = None

        if recorded_characters in (['-'], ['+'], []):
            return 0

        if recorded_characters[0] == '-':
            resulting_int = int(''.join(recorded_characters[1:])) * -1
        elif recorded_characters[0] == '+':
            resulting_int = int(''.join(recorded_characters[1:]))
        else:
            resulting_int = int(''.join(recorded_characters))

        if resulting_int < 2**31 * -1:
            return 2**31 * -1
        elif resulting_int > 2**31 - 1:
            return 2**31 - 1

        return resulting_int


def verbose_assert(*args):
    output = Solution().myAtoi(*args)
    print("Input:  %s\nOutput: %s" % (*args, output))


if __name__ == '__main__':
    args = "-abc"
    verbose_assert(args)
