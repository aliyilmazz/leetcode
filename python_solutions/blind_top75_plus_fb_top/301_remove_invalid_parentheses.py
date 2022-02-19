class Solution:
    def calculate(self, s: str) -> int:

        s += '_'
        reading_digit_mode = False
        operators = {'+', '-', '*', '/', '_'}
        current_number = ''
        stack = []
        previous_operator = '+'
        for char in s:
p
            if char == ' ':
                # skip any whitespace
                continue

            if char.isdigit():
                reading_digit_mode = True
                current_number += char

            else:

                if reading_digit_mode:
                    current_number = int(current_number)
                    reading_digit_mode = False

                # expect operator now
                assert char in operators

                if previous_operator in {'*', '/'}:
                    last_number = stack.pop()
                    if previous_operator == '*':
                        local_result = last_number * current_number
                        stack.append(local_result)
                    elif previous_operator == '/':
                        local_result = int(last_number/current_number)
                        stack.append(local_result)

                else:
                    if previous_operator == '-':
                        current_number *= -1

                    stack.append(current_number)


                previous_operator = char
                current_number = ''

        return sum(stack)










if __name__ == '__main__':
    s = "3+2*2"
    output = Solution().calculate(s)
    print("Input: %s\nOutput: %s" % (s, output))