class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [0] * n
        def dfs(i):
            if i == destination:
                return True
            visited[i] = True
            for j in g[i]:#遍历i的所有邻居
                if not visited[j]:
                    if dfs(j):
                        return True
            return False
        return dfs(source)

#union find
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            else:
                parent[root_x] = root_y

        for u, v in edges:
            union(u, v)
        return find(source) == find(destination)