class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #Count the number of components to calculate operations
        edges = len(connections)

        #1.Pruning
        if edges < n - 1:
            return -1

        #2.Build adjacency list
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        components = 0

        #3.Build visited array
        visited = [False] * n
        def dfs(i: int) -> None:
            nonlocal components
            if visited[i]:#Base case
                return
            visited[i] = True
            for neighbor in g[i]:#Traverse through neighbors
                if not visited[neighbor]:
                    dfs(neighbor)

        #4.Count the number of connected components
        for i in range(n):
            if not visited[i]:
                components += 1
                dfs(i)
        return components - 1