class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """
    完全连通分量：
        用度数法：检查每个节点度数是否等于 m-1。
        用边数法：检查边数是否等于 m*(m-1)/2。
        """
        # For each complete components:
        # The number of edges = size * (size - 1) // 2

        # Build adjacent list for graph
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        count = 0
        visited = [False] * n

        def dfs(i):
            nonlocal size, degree_sum
            if visited[i]:
                return
            # Mark node as visited
            visited[i] = True
            size += 1
            degree_sum += len(g[i])
            # Traverse through neighbors
            for neighbor in g[i]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                size, degree_sum = 0, 0
                dfs(i)
                if size * (size - 1) == degree_sum:
                    count += 1
        return count


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        如果想把变量定义在dfs里面，记得在dfs里return这些变量
        '''
        # For each complete components:
        # The number of edges = size * (size - 1) // 2

        # Build adjacent list for graph
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        count = 0

        visited = [False] * n

        def dfs(i):
            size = 1
            degree_sum = len(g[i])
            # Mark node as visited
            visited[i] = True

            # Traverse through neighbors
            for neighbor in g[i]:
                if not visited[neighbor]:
                    s, d = dfs(neighbor)
                    size += s
                    degree_sum += d
            return size, degree_sum

        for i in range(n):
            if not visited[i]:
                size, degree_sum = dfs(i)
                if size * (size - 1) == degree_sum:
                    count += 1
        return count


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """
    完全连通分量：
        用度数法：检查每个节点度数是否等于 m-1。
		用边数法：检查边数是否等于 m*(m-1)/2。
        """
        g = [[] for _ in range(n)]
        ans = 0
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [0] * n
        def dfs(i):
            if visited[i]:
                return
            component.add(i)
            visited[i] = 1
            for j in g[i]:
                if not visited[j]:
                    dfs(j)
        for i in range(n):
            if not visited[i]:
                component = set()
                dfs(i)
                if all(len(g[i]) == len(component)-1 for i in component):
                    ans+=1
        return ans

#显式传component
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """
    完全连通分量：
        用度数法：检查每个节点度数是否等于 m-1。
		用边数法：检查边数是否等于 m*(m-1)/2。
        """
        g = [[] for _ in range(n)]
        ans = 0
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [0] * n
        def dfs(i, component):
            if visited[i]:
                return
            component.add(i)
            visited[i] = 1
            for j in g[i]:
                if not visited[j]:
                    dfs(j, component)
        for i in range(n):
            if not visited[i]:
                component = set()
                dfs(i, component)
                if all(len(g[i]) == len(component)-1 for i in component):
                    ans+=1
        return ans