class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        #Use dfs and backtrack to store all possible paths from 0 to n - 1
        n = len(graph)
        res = []
        path = []
        def dfs(i):
            path.append(i)
            if i == n - 1:
                res.append(path[:])
                return
            for neighbor in graph[i]:
                dfs(neighbor)
                path.pop()
        dfs(0)
        return res

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #adjlist find way 0 -> n - 1
        if not graph:
            return []
        res = []
        path = []
        n = len(graph)
        def backtracking(i, path):
            if i == n - 1:
                res.append(path[:])
                return
            for j in graph[i]:#j: neighbor
                path.append(j)
                backtracking(j, path)
                path.pop()
        backtracking(0, [0])
        return res
