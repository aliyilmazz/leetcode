from collections import Counter


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        print("asd")
        if not t or not s:
            return ''

        t_chars = Counter(t)
        t_unique_chars_count = len(t_chars)

        left_index, right_index = 0, 0

        formed = 0  # all letter occurrences
        window_counts = dict()

        ans = float('inf'), None, None  # window length, left, right

        while right_index < len(s):

            char = s[right_index]

            if char not in t_chars:
                right_index += 1
                continue

            window_counts[char] = window_counts.get(char, 0) + 1
            if window_counts[char] == t_chars[char]:
                formed += 1

            while left_index <= right_index and formed == t_unique_chars_count:
                #print("entered squeeze state. left right: %s %s" % (left_index, right_index))
                to_be_evicted_char = s[left_index]

                # record highscore
                if ans[0] > right_index - left_index + 1:
                    ans = right_index - left_index + 1, left_index, right_index


                left_index += 1

                if to_be_evicted_char not in t_chars:
                    continue

                window_counts[to_be_evicted_char] = window_counts.get(to_be_evicted_char, 0) - 1
                if window_counts[to_be_evicted_char] < t_chars[to_be_evicted_char]:
                    formed -= 1

            right_index += 1

        #print("final ans: %s" % str(ans))
        return '' if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]


if __name__ == '__main__':
    output = Solution().minWindow("ADOBECODEBANC", "ABC")
    print("output: %s" % output)