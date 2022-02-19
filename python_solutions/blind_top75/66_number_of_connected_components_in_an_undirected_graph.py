from typing import List


class Solution:
    def coinChange_backtrack_false(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)

        '''
        min_coin_count = -1

        def backtrack(target, coin_count):
            nonlocal min_coin_count

            if min_coin_count != -1:
                return  # flag is set. return

            if target < 0:
                return

            if target == 0:
                #min_amount = sum(used_coins.values())
                min_coin_count = coin_count
                return

            for coin in coins:  # always start from biggest coin
                new_target = target - coin
                backtrack(new_target, coin_count+1)

        backtrack(amount, 0)
        '''
        queue = [(amount, 0)]
        while queue:
            target, count = queue.pop()  #  lifo for DFS

            if target == 0:
                return count

            for coin in coins:
                new_target = target - coin
                if new_target < 0:
                    continue
                queue.append((new_target, count + 1))

        return -1

    def _coinChange(self, target, coin_index, coins):

        if target == 0:
            return 0

        if coin_index >= len(coins):
            return -1

        if target < 0:
            return -1

        max_coin_count = int(target / coins[coin_index])  # more than that will cause overflow
        min_total_coin = 99999999

        for current_coin_count in range(max_coin_count + 1):
            current_amount = current_coin_count * coins[coin_index]
            remaining_amount = target - current_amount
            if remaining_amount >= 0:
                total_coins = self._coinChange(remaining_amount, coin_index + 1, coins)  # try other coins
                if total_coins != -1:
                    min_total_coin = min(min_total_coin, total_coins + current_coin_count)

        return min_total_coin if min_total_coin != 99999999 else -1

    def coinChange_bruteforce_TLE(self, coins, amount):
        return self._coinChange(amount, 0, coins)

    def coinChange_topdownDP_auth(self, coins, amount):
        coins = sorted(coins, reverse=True)

        dp = [-2] * (amount + 1)
        # -2 -> undiscovered
        # -1 -> failed
        # we will look for dp[amount]
        #  dp[x] = min coin count to make amount=X

        dp[0] = 0
        for coin in coins:
            if coin < len(dp):
                dp[coin] = 1

        self.min_used_coins = float('inf')

        def f(x, total_used_coins):
            if total_used_coins >= self.min_used_coins:
                return False, None

            if x < 0:
                return False, None

            if dp[x] == -1:
                return False, None  # failed

            if dp[x] != -2:  # outside undiscovered
                return True, dp[x]

            min_amount = float('inf')
            for coin in coins:
                if x-coin < 0:
                    continue
                success, amt = f(x - coin, total_used_coins + 1)
                if success:
                    new_coin_amount = amt + 1
                    min_amount = min(min_amount, new_coin_amount)
                    if x == amount:
                        self.min_used_coins = min(self.min_used_coins, new_coin_amount)


            if min_amount == float('inf'):
                dp[x] = -1
                return False, -1
            else:
                dp[x] = min_amount
                return True, min_amount

        total_used_coins = 0
        result = f(amount, total_used_coins)[1]
        return result if result != float('inf') else -1

    def coinChange(self, coins, amount):

        dp = [0] * (amount + 1)
        dp[0] = 0


        def _coinChange(amount):
            if amount < 0:
                return -1

            if amount == 0:
                return 0

            if dp[amount] != 0:
                return dp[amount]

            min_count = float('inf')
            for coin in coins:
                result = _coinChange(amount - coin)
                if 0 <= result < min_count:
                    min_count = result + 1

            dp[amount] = min_count if min_count != float('inf') else -1
            return dp[amount]

        return _coinChange(amount)

if __name__ == '__main__':
    #coins = [1, 2, 5]
    #amount = 11
    coins = [186,419,83,408]
    amount = 6249
    output = Solution().coinChange(coins, amount)
    print("coins: %s, target: %s, output: %s" % (coins, amount, output))