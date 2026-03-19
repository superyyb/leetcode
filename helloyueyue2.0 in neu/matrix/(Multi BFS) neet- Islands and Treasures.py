from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #multi BFS 把所有作为BFS起点的格子的index(i, j)入队
        """
        1. base case + n, m
        2.matrix双层遍历list单层,存放各个BFS起点到q
        3.如果是matrix 需要有上下左右的directions
        4.while q:
            a.pop
            b.遍历directions,计算出新的nx,ny
            c.check nx, ny是否满足条件(不越界,是通路)
            d.按题目要求update nx, ny
            e.最后别忘了把得到的updated nx,ny append进入q
        """
        if not grid or not grid[0]:
            return #return nothing: modify in place
        n = len(grid)
        m = len(grid[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))#⚠️这里只需要(i, j)进入q，而不是grid[i][j]
        INF = 2147483647
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))
        #no return: modify in place

#multi DFS
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        grid:
          - 0   : treasure / gate
          - -1  : wall
          - INF : empty room
        After: each INF becomes distance to nearest 0
        """
        if not grid or not grid[0]:
            return
        m, n = len(grid), len(grid[0])
        INF = 2147483647

        def dfs(r, c, dist) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == -1:
                return
            if grid[r][c] < dist:  # 当前dist更大，return
                return
            grid[r][c] = dist  ##当前dist更小，更新格子为dist

            dfs(r + 1, c, dist + 1)
            dfs(r - 1, c, dist + 1)
            dfs(r, c + 1, dist + 1)
            dfs(r, c - 1, dist + 1)

        # multi DFS：从所有 gate/treasure（值为 0 的格子）出发
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 0)