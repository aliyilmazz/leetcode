from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:




if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    combinations = Solution().combinationSum(candidates, target)
    print("Candidates: %s\nTarget:%s\nCombinations: %s" % (candidates, target, combinations))