from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        '''
        multi BFS
        1.Start from land, use BFS to find the water
          Round 1: find the water whose distance is 1
          Round 2: find the water whose distance is 2
          ...
          Eventually find the water which has max distance
        2.No need of |x0 - x1| + |y0 - y1|
        3.Everytime find a land, update the max distance
        4.Edge case: visited, whether it is land
        '''
        n = len(grid)
        if n == 1:
            return -1
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        # edge cases: all water or all land
        if not q or len(q) == n * n:
            return -1

        dist = -1
        distance = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                for dr, dc in distance:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:  # 忘记越界条件
                        grid[nr][nc] = 1
                        q.append((nr, nc))
            dist += 1
        return dist







