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
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        perimeter = 0
        visited = [[0] * col for _ in range(row)]#⚠️visited for matrix
        def dfs(i, j):
            nonlocal perimeter
            if (i < 0 or i >= row or j < 0 or j >= col
            or grid[i][j] == 0 or visited[i][j] == 1):
                return
            visited[i][j] = 1
            perimeter += 4
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (0 <= x < row and 0 <= y < col
                and visited[x][y] == 1 and grid[x][y] == 1):
                    perimeter -= 2
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(i, j)
        return perimeter