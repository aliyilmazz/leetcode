from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        '''

        * as we traverse, record indices

        * if we come across `close` when stack is NULL
            * remove one of prev closes (if any) or remove self


        * at the end, if we have N open parentheses,
            remove last N open parentheses


        '''


        results = []
        N = len(s)

        def get_to_be_deleted_indices(s, open, close):
            n = len(s)
            i = 0

            to_be_deleted_indices = []
            closes = []
            counter = 0


            while i<n:
                char = s[i]

                if char not in [open, close]:
                    i += 1
                    continue

                if char == open:
                    counter += 1
                    i += 1
                    continue

                if char == close:
                    if counter == 0:
                        # eg: '()())'
                        temp_i = i
                        count = 0
                        temp_i = i
                        while temp_i<n and s[temp_i] != open:
                            if s[temp_i] not in [open, close]:
                                temp_i += 1
                                continue  # non-parenthesis chars
                            closes.append(temp_i)
                            count += 1
                            temp_i += 1

                        for _ in range(count):
                            to_be_deleted_indices.append(closes.copy())
                        #closes = []
                        i = temp_i
                        continue
                    else:
                        closes.append(i)
                        counter -= 1
                        i += 1
                        continue

            print("s: %s, indices: %s" % (s, to_be_deleted_indices))
            return to_be_deleted_indices

        to_be_deleted_indices = get_to_be_deleted_indices(s, '(', ')')
        reversed_str = s[::-1]
        reverse_indices = get_to_be_deleted_indices(reversed_str, ')', '(')
        for reverse_index_set in reverse_indices:
            index_set = [N-1-element for element in reverse_index_set]
            to_be_deleted_indices.append(index_set)


        # todo: compile results
        print("to be deleted indices: %s" % to_be_deleted_indices)
        indices = []
        for record in to_be_deleted_indices:
            if not indices:
                indices = [[r] for r in record]
            else:
                new_indices = []
                for prev_option in indices:
                    for new_option in record:
                        if new_option not in prev_option:
                            new_indices.append(prev_option + [new_option])
                indices = new_indices

        if not indices:
            return [s]

        #print("indices: %s" % indices)
        for option in indices:
            new_str = ''.join([char for i, char in enumerate(s) if i not in option])
            results.append(new_str)

        return list(set(results))


if __name__ == '__main__':
    # results = Solution().removeInvalidParentheses("()())()")
    # print("results: %s" % results)
    #
    # results = Solution().removeInvalidParentheses("(()))")
    # print("results: %s" % results)
    #
    # results = Solution().removeInvalidParentheses(")(")
    # print("results: %s" % results)

    # results = Solution().removeInvalidParentheses("(r(()()(")
    # print("results: %s" % results)
    #
    # results = Solution().removeInvalidParentheses("((()()(")
    # print("results: %s" % results)

    results = Solution().removeInvalidParentheses("(((()(()")
    print("results: %s" % results)