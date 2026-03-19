from collections import defaultdict
from collections import deque
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        if matrix[0][0] == "#":
            return -1
        m, n = len(matrix), len(matrix[0])
        letters = defaultdict(list)
        for r in range(m):
            for c in range(n):
                if matrix[r][c].isalpha():
                    letters[matrix[r][c]].append((r, c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dist = [[float('inf')] *  n for _ in range(m)]#用 dist 2d数组记录每个格子从起点开始的最短dist
        dist [0][0] = 0
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            d = dist[x][y]
            if x == m - 1 and y == n - 1:
                return d
            cell = matrix[x][y]
            if cell in letters:#考虑传送门0代价的情况
                for lx, ly in letters[cell]:
                    if d < dist[lx][ly]:
                        dist[lx][ly] = d
                        q.appendleft((lx, ly))
                del letters[cell] #避免重复使用传送门
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != "#":
                    if d + 1 < dist[nx][ny]:
                        dist[nx][ny] = d + 1
                        q.append((nx, ny))
        return - 1