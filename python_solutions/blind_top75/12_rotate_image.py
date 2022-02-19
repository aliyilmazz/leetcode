class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(target, combination):

            if target == 0:
                results.append(tuple(sorted(combination)))
                return

            for candidate in candidates:
                new_target = target - candidate
                if new_target < 0:
                    continue

                if combination and candidate < combination[-1]:
                    continue

                combination.append(candidate)
                backtrack(new_target, combination)
                combination.pop()

        backtrack(target, [])
        # return list(set(results))
        return results