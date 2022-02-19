class Solution(object):

    def lengthOfLongestSubstring(self, s):
        substring_char_set = set()
        #substring = ""
        length = 0
        record_length = 0
        left_index = 0
        right_index = 0

        for char in s:
            if char not in substring_char_set:
                right_index += 1
                substring_char_set.add(char)
            else:
                length_before_truncation = (right_index - left_index)
                record_length = max(record_length, length_before_truncation)
                right_index += 1
                while left_index < right_index - 1:
                    if s[left_index] == char:
                        left_index += 1
                        break  # bump by one, and exit truncation
                    else:
                        substring_char_set.remove(s[left_index])
                        left_index += 1


        return max(record_length, (right_index-left_index))


if __name__ == '__main__':
    s = "bbbbb"
    print("Input:%s\nOutput:%s" % (s, Solution().lengthOfLongestSubstring(s)))

    s = "abcabcbb"
    print("Input:%s\nOutput:%s" % (s, Solution().lengthOfLongestSubstring(s)))

    s = "pwwkew"
    print("Input:%s\nOutput:%s" % (s, Solution().lengthOfLongestSubstring(s)))

    s = ""
    print("Input:%s\nOutput:%s" % (s, Solution().lengthOfLongestSubstring(s)))

    s = "aab"
    print("Input:%s\nOutput:%s" % (s, Solution().lengthOfLongestSubstring(s)))

    s = "dvdf"
    print("Input:%s\nOutput:%s" % (s, Solution().lengthOfLongestSubstring(s)))


