#笨蛋recursion
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

#标准dp
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:#不能省略，防止题目给的n<2，越界
            return n
        dp = [0] * (n + 1)  # 确定dp数组
        dp[0] = 0  # 初始化
        dp[1] = 1
        for i in range(2, n + 1):  # 遍历顺序
            dp[i] = dp[i - 1] + dp[i - 2]  # 递推公式
        return dp[n]

#节省空间dp（一）
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0, 1]
        for i in range(2, n + 1):
            total = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = total

        return dp[1]
#节省空间dp（二）
class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

