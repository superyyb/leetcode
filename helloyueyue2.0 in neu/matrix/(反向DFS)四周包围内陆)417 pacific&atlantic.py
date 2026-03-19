class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #分别从Pac和Atl出发，淹没可以到达的陆地，取交集
        res = []
        if not heights or not heights[0]:
            return []
        m = len(heights)
        n = len(heights[0])
        pac = set()
        atl = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j, visit, preHeight):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if heights[i][j] < preHeight:
                return
            if (i, j) in visit:
                return
            visit.add((i, j))
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                dfs(nr, nc, visit, heights[i][j])#⚠️更新preHeight为当前h
        for i in range(m):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, n - 1, atl, heights[i][n - 1])
        for j in range(n):
            dfs(0, j, pac, heights[0][j])
            dfs(m - 1, j, atl, heights[m - 1][j])
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res