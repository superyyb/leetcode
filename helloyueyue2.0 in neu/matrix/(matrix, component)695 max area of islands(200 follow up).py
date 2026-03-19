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

#11.26复盘：
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Use DFS to traverse through grid
        # Count the size of each component and find the largest one
        # Use max_area to store and update the maximum island area
        # Mark the land as 0 if I have visited it

        if not grid or not grid[0]:  # To avoid [[]]
            return 0
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        area = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            nonlocal area
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            # Mark the visited land as 0
            grid[r][c] = 0
            area += 1#⚠️不要吧 area += 1 放在下面的for loop里
            # Traverse through neighbors
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0 # ⚠️⚠️记住area清零
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