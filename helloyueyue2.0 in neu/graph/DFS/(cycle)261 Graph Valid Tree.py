class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Tree: All nodes should be connected and acyclic
        #Any two nodes have exactly one path. edges = n - 1
        '''
        先判断边数是否等于n-1,不满足直接return False
        再判断是否只有一个component
        '''
        if len(edges) != n - 1:
            return False
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [False] * n
        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            for neighbor in g[i]:
                if not visited[neighbor]:
                    dfs(neighbor)
        dfs(0)
        return visited == [True] * n

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
    Definition of a tree:
    1.An undirected graph with no cycles
    2.All the nodes are connected as one component
    3.Any two nodes have exactly one path. 边数= n - 1
        """
        """
    在 DFS 遍历时，每条边 (u, v) 会出现两次：
	•一次从 u 走到 v；
	•一次从 v 走到 u。
    别把“回到父节点”误认为是环。
        """
        if len(edges) != n - 1: #条件3
            return False
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [0] * n
        def dfs(i, parent):#条件2
            if not visited[i]:
                visited[i] = 1
                for j in g[i]:
                    if not visited[j]: #if j not visited
                        if dfs(j, i):
                            return True
                    elif j != parent: #elif j visited
                        return True
            return False
        if dfs(0, -1):# 从0出发,一次性遍历
            return False
        return visited == [1] * n#判断所有节点是否都已经访问过（图是否连通）
        #或者写成return all(visited)

