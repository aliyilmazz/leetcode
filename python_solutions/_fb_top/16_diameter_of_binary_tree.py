class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        if not n:
            return

        prefix_sum = []
        modulo_dict = dict()
        total_sum = 0
        modulo_dict[0] = -1
        for idx, num in enumerate(nums):
            total_sum += num
            total_sum %= k
            if total_sum in modulo_dict:
                prev_idx = modulo_dict[total_sum]
                if prev_idx < idx - 1:
                    return True
            else:
                modulo_dict[total_sum] = idx

        return False
