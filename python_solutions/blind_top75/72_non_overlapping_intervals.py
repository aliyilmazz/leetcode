from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if not n:
            return 0

        counter = Counter()

        left, right = 0, 0
        max_length = 1
        while right < n:
            letter = s[right]
            counter[letter] += 1

            most_common_letter, most_common_letter_count = counter.most_common()[0]
            current_substring_length = right - left + 1

            while current_substring_length - most_common_letter_count > k:
                counter[s[left]] -= 1
                left += 1
                current_substring_length -= 1
                _, most_common_letter_count = counter.most_common()[0]
                # we need to shrink window

            max_length = max(max_length, current_substring_length)

            right += 1

        return max_length









