class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        #只要找到和1连通的所有edges的最小值
        min_val = float('inf') #⚠️val可能会小于0
        if n == 1:
            return 0
        g = [[] for _ in range(n + 1)]#⚠️不能写len(roads),因为可能有的city没有edges不在这个list里面
        for u, v, val in roads:
            g[u].append((v, val))
            g[v].append((u, val))
        visited = [0] * (n + 1)
        def dfs(i):
            nonlocal min_val
            if visited[i]:
                return
            visited[i] = 1
            for j, val in g[i]:
                min_val = min(min_val, val)
                if not visited[j]:
                    dfs(j)
        dfs(1) #不要惯性思维for i in range(n + 1)，这道题只需要找到dfs(1)就行
        return min_val