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
                    count = grid[r][c]
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