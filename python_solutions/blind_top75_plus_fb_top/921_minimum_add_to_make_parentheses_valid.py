class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        '''
        keep a stack

        for each char:
            * if see open parenthesis, add it to stack
            * if closing parenthesis:
                * if stack not empty: pop one from stack
                * else: add_counter += 1


        * if stack non empty:
            * add_counter += stack.size()


        return add_counter

        '''

        minimum_add_count = 0
        open_parenthesis_count = 0

        for char in s:
            if char == '(':
                open_parenthesis_count += 1
            else:
                if open_parenthesis_count > 0:
                    open_parenthesis_count -= 1
                else:
                    minimum_add_count += 1

        minimum_add_count += open_parenthesis_count

        return minimum_add_count


if __name__ == '__main__':
    s = '()))'
    output = Solution().minAddToMakeValid(s)
    print("string: %s, output: %s" % (s, output))
