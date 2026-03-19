class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # ⚠️从边界淹没陆地
        # 先把所有边界上的 1 出发做 DFS/BFS，把能到达的陆地都淹成 0；
        # 扫一遍网格，剩下的 1 的个数就是答案。
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):

            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            grid[r][c] = 0
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)

        for i in range(m):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][n - 1] == 1:
                dfs(i, n - 1)
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[m - 1][j] == 1:
                dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        return count

#BFS解法 time O(m*n) space: worst O(m*n)
from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        BFS:
        Start from cell'1' in the four boundaries of grid and push their coordinates into queue
        Use bfs to find all connected components and mark them
        return the number of existing cell'1's
        '''
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            if grid[i][0] == 1:
                q.append((i, 0))
                grid[i][0] = 0
            if grid[i][n - 1] == 1:
                q.append((i, n - 1))
                grid[i][n - 1] = 0
        for j in range(n):
            if grid[0][j] == 1:
                q.append((0, j))
                grid[0][j] = 0
            if grid[m - 1][j] == 1:
                q.append((m - 1, j))
                grid[m - 1][j] = 0
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    q.append((nr, nc))
                    grid[nr][nc] = 0
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        return count






