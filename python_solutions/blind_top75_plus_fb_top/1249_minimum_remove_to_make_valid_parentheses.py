class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''
            * skim through the string
            * #keep a index->parenthesis map
            * keep a stack for opening-closing parentheses (store index)
            * keep a index->valid map


            * as we traverse chars in string:
                * add them to index->valid map as invalid (by default)
                * if opening, add index to stack
                * if closing, pop last index from stack, mark that index as valid (in first map)
            * after traversal:
                * see index -> valid map, remove all invalid indices
                * return string

        '''

        #index_validation_map = dict()  # index to boolean mapping.
        parenthesis_stack = []  # holds index as key.
        invalid_indices = []

        for _index, char in enumerate(s):
            #print("map:%s" % index_validation_map)
            print("stack:%s" % parenthesis_stack)
            if char not in ['(', ')']:
                continue  #  skip non-parenthesis characters

            #index_validation_map[_index] = False  # all parentheses are invalid by default

            if char == '(':
                parenthesis_stack.append(
                    _index)  # store index, so that we can know what index to whitelist once we mean to pop it

            else:
                if not parenthesis_stack:
                    invalid_indices.append(_index)
                    continue

                parenthesis_stack.pop()
                # index_validation_map[to_be_whitelisted_index] = True
                # index_validation_map[_index] = True

        print("iterations ended")
        #print("map:%s" % index_validation_map)
        print("stack:%s" % parenthesis_stack)
        # for _index, _valid in index_validation_map.items():
        #     if _valid:
        #         continue
        #
        #     s = s[:_index] + s[_index + 1:]

        #invalid_indices = [key for key in index_validation_map.keys() if index_validation_map[key] == False]
        #invalid_indices.extend(parenthesis_stack)



        _s = ''.join(char for _index, char in enumerate(s) if _index not in invalid_indices and _index not in parenthesis_stack)

        return _s


if __name__ == '__main__':
    s = "lee(t(c)o)de)"
    output = Solution().minRemoveToMakeValid(s)
    print("Input: %s\nOutput: %s" % (s, output))

    s = "))(("
    output = Solution().minRemoveToMakeValid(s)
    print("Input: %s\nOutput: %s" % (s, output))
