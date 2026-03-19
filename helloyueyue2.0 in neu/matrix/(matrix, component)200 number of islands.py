"""
模版：在递归函数外面 遍历过程中累加结果
    1.base case + n, m
    2. def(dfs)
        a.base case to return
        b.mark grid[i][j] == visited
        c.call dfs in dfs
    3.traverse(matrix: 双层遍历, adjlist: 单层遍历)
        a.if grid[i][j] == 1: call dfs + 计数
        b.return result
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n = len(grid) #row
        m = len(grid[0]) #col
        def dfs(i, j): #dfs 只是负责把这一整块岛屿淹没，防止重复计数。
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "0":# 极限：i=0,i=n-1
                return#遇到已经visited或者边界或者水域，直接return
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #do dfs to node:find its neighbour, turn 1 to 0, do dfs to its neighbor
        #outside dfs: count how many times to do dfs
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        #再次写：写了visited 其实这道题不用
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        def dfs(i, j):#再次写：忘记越界条件
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for di, dj in directions:
                ni, nj = i + di, j + dj
                # if grid[nr][nc] == '1':  再次写：⚠️不要加这句，dfs已经判断了这个case
                dfs(ni, nj)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count