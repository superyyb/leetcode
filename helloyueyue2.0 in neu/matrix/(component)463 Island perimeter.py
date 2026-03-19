#不用dfs 直接暴力遍历Normal traversal
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
         #when finding a land, add 4 to answer while checking if (i - 1, j) and (i, j - 1) is also land, if so, minus 2
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        perimeter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j] == 1:#⚠️一定要加i > 0
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2
        return perimeter
    """
如果用dfs不可以用上面的方法：“每个陆地 +4，和已存在的上/左陆地各 −2” 这个规则依赖固定的扫描顺序
（如按行从左到右、从上到下），而 DFS 的访问顺序是不固定的（会先沿着某条路径深挖到很远再回溯），
所以不能保证你到达某个格子时，它的“上/左”正好就是“先访问过的那个相邻格子”。
结果就是：有的共享边不会在“第二次”被看到（从“上/左”角度），导致漏减或重复计数。
    """

#硬要用dfs的话，改成“对四个方向，只要邻居是‘已访问的陆地’就 −2”。需要设立一个visited储存已访问
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #1. Everytime we find a cell, add 4 to perimeter
        #2. Everytime we find an adjacent pair, minus 2 to the perimeter
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r: int, c: int) -> None:
            nonlocal perimeter
            #1. Base/invalid case
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if grid[r][c] == 0 or visited[r][c]:
                return
            #2. Mark cell as visited and add to perimeter
            visited[r][c] = True
            perimeter += 4
            #3. Spread and do dfs to its neighbors
            for dr, dc in directions:#邻居如果是陆地，则共享边，-2
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and visited[nr][nc]:
                    perimeter -= 2
                    dfs(nr, nc)
            #4. Traverse through grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
        return perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #Everytime we find a cell that is land and adjacent to water/boundary,
        #add 1 to perimeter
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(r: int, c: int) -> int:
        #1. Meet water/boundary, add 1 to perimeter
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 1
        #2. If visited, no contribution to perimeter
            if visited[r][c]:
                return 0
        #3. Mark cell as visited
            visited[r][c] = True
            perimeter = 0
        #4. Traverse through neighbors
            perimeter += dfs(r-1, c)
            perimeter += dfs(r+1, c)
            perimeter += dfs(r, c-1)
            perimeter += dfs(r, c+1)
            return perimeter
        #5. Find the land to start
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j)

#❌经典错误
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #If I meet boundary/water, add 1 to perimeter
        #DFS
        # if not grid or not grid[0]:
        #     return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r: int, c: int) -> int:
            #Check invalid cases and return
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 1
            if visited[r][c]:
                return 0
            #Mark the cell as visited
            visited[r][c] = True
            #Traverse through neighbors
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if not visited[nr][nc]:
                    return dfs(nr, nc) #dfs只会return一个方向的结果
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    return dfs(i, j)

#perimeter作为全局变量
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #If I meet boundary/water, add 1 to perimeter
        #DFS
        # if not grid or not grid[0]:
        #     return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        perimeter = 0
        def dfs(r: int, c: int) -> int:
            nonlocal perimeter
            #Check invalid cases and return
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                perimeter += 1
                return
            if visited[r][c]:
                return
            #Mark the cell as visited
            visited[r][c] = True
            #Traverse through neighbors
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)
                    return perimeter