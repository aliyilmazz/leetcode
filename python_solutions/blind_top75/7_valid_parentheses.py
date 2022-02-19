class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ''' 
            we can have open parentheses in any order

            for each close:
                make sure it closes last open parentheses.

            after all:
                make sure stack is empty


            ***
                keep a mapping for open-close pairs
                for each char:
                    if its a key, register it on stack
                    else, see whats on top of stack. 
                        if map true, then pop stack, go on
                        else, return false
                if stack not empty, return false
                else return true
            ***




        '''

        parentheses = {'{': '}', '(': ')', '[': ']'}
        openings = {"(", "[", "{"}

        stack = []
        for char in s:
            if char in openings:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                last_open_parenthesis = stack[-1]
                if parentheses[last_open_parenthesis] != char:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        else:
            return True


