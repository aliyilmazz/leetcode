from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_streak = 0
        num_set = set(nums)
        visited_nums = set()

        for num in nums:
            if num in visited_nums:
                continue  # we have covered this range. skip re-processing it

            visited_nums.add(num)
            current_streak = 1  # the `num` itself makes streak start from 1

            # [1] traverse left side of num, register visited nums to avoid re-processing
            negative_traverser = num - 1
            while negative_traverser in num_set and negative_traverser not in visited_nums:
                current_streak += 1
                visited_nums.add(negative_traverser)
                negative_traverser -= 1

            # if we have exited while loop due to visited_num violation,
            # skip processing right side
            if negative_traverser in visited_nums:
                continue

            # [2] traverse right side of num
            positive_traverser = num + 1
            while positive_traverser in num_set and positive_traverser not in visited_nums:
                current_streak += 1
                visited_nums.add(positive_traverser)
                positive_traverser += 1

            if positive_traverser in visited_nums:
                continue

            # record the value
            longest_streak = max(longest_streak, current_streak)

        return longest_streak