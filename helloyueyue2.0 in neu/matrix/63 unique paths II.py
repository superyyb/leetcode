class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 遇到障碍时，跳过递归累加dp[i][j]公式
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:  # base case
            return 0
        dp = [[0] * n for _ in range(m)]  # 定义dp数组
        for i in range(m):  # 初始化
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):  # 只有确保第一行第一列已经初始化了，才可以从1,m 1,n开始遍历
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    """
    为什么初始化遇到障碍可以直接break：
    如果第一列某个格子是障碍（例如 [2][0] 是障碍），那么它以下的格子（如 [3][0]）：
	•	没有任何办法从起点走到那里（因为上面被障碍挡住）
	•	所以 dp[i][0] = 0，不用再赋值了，第一行同理
    因此直接 break，节省不必要的赋值。
    """

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #只有不遇到障碍时，dp[i][j]才可以进行递推累加
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        dp = [[0] * n for _ in range(m)] #定义dp数组
        for i in range(m): #初始化
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]