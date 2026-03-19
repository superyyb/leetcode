class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1#递推公式依赖两个前项，所以必须初始化两个值
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

"""
    场景	dp[i] 数组	                       dp 初始值	                     举例
计数型(int),有多少种方法                   [0] * (n + 1)	            LC70 Climbing Stairs
可达型（True/False）	能否到达某状态	    [False] * n	                LC55 Jump Game
最值型（min/max）	最小/最大代价	        [inf] * n 或 [-inf] * n  	    最短路径、打家劫舍等
字符串/路径型	str/list	        [""] * n 或 [[] for _ in range(n)]	输出路径、组合类题
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        因为dp[i]只和前两项有关，因此可以优化为O(1)空间
        a代表dp[i - 2]，b代表dp[i - 1]
        每次迭代后更新为：
	•	新的 a ← 旧的 b（dp[i - 1]）
	•	新的 b ← 旧的 a + b（dp[i]）
        """
        if n == 0 or n == 1:
            return 1
        a, b = 1, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b