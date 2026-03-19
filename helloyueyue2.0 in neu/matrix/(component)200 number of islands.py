"""
模版：在递归函数外面 遍历过程中累加结果
    1.base case + n, m
    2. def(dfs)
        a.base case to return
        b.mark grid[i][j] == visited
        c.call dfs in dfs
    3.traverse(matrix: 双层遍历, adjlist: 单层遍历)
        a.if grid[i][j] == 1: call dfs + 计数
        b.return result
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n = len(grid) #row
        m = len(grid[0]) #col
        def dfs(i, j): #dfs 只是负责把这一整块岛屿淹没，防止重复计数。
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "0":# 极限：i=0,i=n-1
                return#遇到已经visited或者边界或者水域，直接return
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i, j - 1)#⚠️直接把 grid[i][j] 改成'0'，不需要再判断一遍base case
            dfs(i + 1, j)
            dfs(i, j + 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count

#直接四个方向一起写
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        visit = [[False] * n for _ in range(m)]
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or visit[r][c] or grid[r][c] == "0":
                return
            visit[r][c] = True
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c#⚠️重新设置一个二维数组标记，所以需要再次判断base case
                if 0 <= nr < m and 0 <= nc < n and not visit[nr][nc] and grid[nr][nc] != "0":
                    dfs(nr, nc)
        count = 0
        for r in range(m):
            for c in range(n):
                if not visit[r][c] and grid[r][c] != "0":
                    count += 1
                    dfs(r, c)
        return count