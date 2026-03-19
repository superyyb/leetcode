class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        # figure out the number of connected components whose size can be divided by k
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        count = 0
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            val = grid[i][j]  # ✅ 先取出当前格子的数值
            grid[i][j] = 0  # 再标记已访问（就地淹没）
            return val + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    total = dfs(i, j)
                    if total % k == 0:
                        count += 1
        return count

    """
    二维list判空：
    if not grid: 只会检查 外层 list 是否为空。
    if not grid[0] 检查第一行有没有“列”。
    双重check才能保证判空
    eg: grid = [[]]，not grid == False，但是 m = len(grid[0])会报错
    """

#accumulator
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        count = 0
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        visit = [[False] * n for _ in range(m)]
        def dfs(r, c):
            nonlocal total
            if r < 0 or r >= m or c < 0 or c >= n or visit[r][c] or grid[r][c] == 0:
                return
            visit[r][c] = True
            total += grid[r][c]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and not visit[nr][nc]:
                    dfs(nr, nc)
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0 and not visit[r][c]:
                    total = 0 #total每次重置
                    dfs(r, c)
                    if (k == 0 and total == 0) or (k != 0 and total % k == 0):#stronger in case k == 0 then total % k will cause error
                        count += 1
        return count