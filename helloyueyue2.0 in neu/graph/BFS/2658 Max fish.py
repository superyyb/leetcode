from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        #multi-BFS
        max_count = count = 0
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:#启动一次bfs
                    q = deque([(r, c)])
                    count = grid[r][c]#⚠️这个步骤其实是每次bfs重置count
                    grid[r][c] = 0
                    while q:
                        rr, cc = q.popleft()
                        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        for dr, dc in directions:
                            nr, nc = dr + rr, dc + cc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0:
                                count += grid[nr][nc]
                                grid[nr][nc] = 0
                                q.append((nr, nc))
                    max_count = max(max_count, count)
        return max_count

#外部累加器
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        count = max_count = 0
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j):
            nonlocal count
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            count += grid[i][j]
            grid[i][j] = 0
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                dfs(nr, nc)
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    count = 0
                    dfs(i, j)
                    max_count = max(max_count, count)
        return max_count

#依赖返回值
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_count = 0
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            count = grid[i][j]
            grid[i][j] = 0
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                count += dfs(nr, nc)
            return count
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_count = max(max_count, dfs(i, j))
        return max_count