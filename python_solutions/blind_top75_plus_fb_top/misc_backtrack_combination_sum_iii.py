from typing import List

class Solution:

    def _combinationSum3(self, k, candidates, target, sum_elements):

        if k == 1:
            if target in candidates and target not in sum_elements:
                sum_elements.add(target)
                return True, [sorted(list(sum_elements))]
            else:
                return False, None

        combinations = []
        copy_candidates = candidates.copy()
        for candidate in candidates:
            if candidate > target:
                continue

            # prepare next level
            copy_candidates.remove(candidate)

            copy_sum_elements = sum_elements.copy()
            copy_sum_elements.add(candidate)

            new_target = target - candidate

            new_combinations_exist, new_combinations = self._combinationSum3(k - 1, copy_candidates, new_target, copy_sum_elements)

            print("k:%s, candidates: %s, sum_elements:%s, target:%s, Bool: %s, Comb: %s" % (
                k, copy_candidates, copy_sum_elements, new_target, new_combinations_exist, new_combinations)
            )

            if new_combinations_exist:
                combinations.extend(new_combinations)

            # backtrack
            # copy_candidates.add(candidate)

        if combinations:
            return True, combinations
        else:
            return False, []

    def combinationSum3_intuitive(self, k: int, n: int):
        candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        return self._combinationSum3(k, candidates, n, set())[1]

    def combinationSum3(self, k, n):
        results = []

        def backtrack(target, comb, next_start):
            if len(comb) == k:
                if target == 0:
                    results.append(list(comb))
                return

            for i in range(next_start, 9):

                new_target = target - i
                if new_target < 0:
                    continue

                comb.append(i)  # build up combination
                backtrack(new_target, comb, i + 1)
                comb.pop()

        backtrack(n, [], 0)


if __name__ == '__main__':
    combinations = Solution().combinationSum3(3, 9)
    print("combinations: %s" % combinations)
