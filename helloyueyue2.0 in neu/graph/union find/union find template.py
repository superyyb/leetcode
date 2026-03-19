class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        #只要 A ，B，C 在同一个root下就是同一个集合。
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:#发现同一个root, 说明在一个集合，不用相连直接返回
                return False
            else:
                parent[root_x] = root_y#连接

        for u, v in edges:
            union(u, v)
        return find(source) == find(destination)