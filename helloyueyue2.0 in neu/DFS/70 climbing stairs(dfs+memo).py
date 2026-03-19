class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} # 记录从第 i 阶到终点有多少种走法
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:#查账
                return memo[i]
            memo[i] = dfs(i + 1) + dfs(i + 2)#记账
            return memo[i]
        return dfs(0)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)#类似于visited
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if memo[i] != -1:#已被访问过
                return memo[i]
            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        return dfs(0)