class Solution:
    def longestValidParentheses_stack(self, s: str) -> int:
        max_length = 0

        left_stack_counter = 0
        local_length_from_left = 0
        for char in s:
            if char == '(':
                left_stack_counter += 1
                local_length_from_left += 1
            elif char == ')':
                if left_stack_counter == 0:
                    local_length_from_left = 0
                    left_stack_counter = 0
                else:
                    left_stack_counter -= 1
                    local_length_from_left += 1
                    if left_stack_counter == 0:
                        max_length = max(max_length, local_length_from_left)

        right_stack_counter = 0
        local_length_from_right = 0

        for char in reversed(s):
            if char == ')':
                right_stack_counter += 1
                local_length_from_right += 1
            elif char == '(':
                if right_stack_counter == 0:
                    local_length_from_right = 0
                    right_stack_counter = 0
                else:
                    right_stack_counter -= 1
                    local_length_from_right += 1
                    if right_stack_counter == 0:
                        max_length = max(max_length, local_length_from_right)

        return max_length

    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = []
        stack.append(-1)

        for _index, char in enumerate(s):
            if char == '(':
                stack.append(_index)
            elif char == ')':
                stack.pop()
                if not stack:
                    stack.append(_index)  # this index is not valid. add for future ref
                else:
                    max_length = max(max_length, _index - stack[-1])
        return max_length



