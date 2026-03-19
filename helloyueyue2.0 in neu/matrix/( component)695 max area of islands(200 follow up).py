#外部累加器
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        area = 0
        def dfs(i, j):
            nonlocal area
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return
            grid[i][j] = 0
            area += 1
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            return area
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = 0   #⚠️ 遇到新岛，面积清零
                    dfs(i, j)
                    max_area = max(max_area, area)
        return max_area

#依赖返回值
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #return max size of component
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        def dfs(i, j):#⚠️依赖返回值一定要注意return里面要有东西
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area

#显式传参area 不推荐
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        def dfs(i, j, area):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return area
            grid[i][j] = 0
            area += 1
            area = dfs(i - 1, j, area)
            area = dfs(i + 1, j, area)
            area = dfs(i, j - 1, area)
            area = dfs(i, j + 1, area)
            return area
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j, 0))
        return max_area