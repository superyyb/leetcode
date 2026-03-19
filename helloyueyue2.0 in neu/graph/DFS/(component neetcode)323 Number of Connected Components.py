class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [0] * n
        def dfs(i):
            if visited[i]:
                return
            visited[i] = 1
            for j in g[i]:
                if not visited[j]:
                    dfs(j)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count