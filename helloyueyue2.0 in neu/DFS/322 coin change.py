class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}#Store how many coins do I need to reach amount
        def dfs(curr):
            if curr == amount:
                return 0
            if curr > amount:
                return float('inf')
            if curr in memo:
                return memo[curr]
            memo[curr] = float('inf')
            for coin in coins:
                sub_res = dfs(curr + coin)
                if sub_res != float('inf'):
                    memo[curr] = min(memo[curr], sub_res + 1)
            return memo[curr]
        result = dfs(0)
        return result if result != float('inf') else -1



class Solution:
    def coinChange(self, coins, amount):

        @lru_cache(maxsize=None)
        def dfs(curr):
            if curr > amount:
                return math.inf
            if curr == amount:
                return 0
            return min(dfs(curr + val) + 1 for val in coins)

        result = dfs(0)

        return -1 if result == math.inf else result