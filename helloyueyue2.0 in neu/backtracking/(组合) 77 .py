class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex, n - (k - len(path))+ 2):
                path.append(i)
                backtracking(i + 1)
                path.pop()
        backtracking(1)
        return res

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtracking(n, k, 1, [], res)
        return res
    def backtracking(self, n, k, startindex, path, res):
        if len(path) == k:
            res.append(path[:])
            return #这条路径已经完成，不需要再深入递归了
        for i in range(startindex, n + 1):
            path.appe6nd(i)
            self.backtracking(n, k, i + 1, path, res)
            path.pop()
    """
    回溯过程中，path 会不断 .append() 和 .pop()，所以它一直在被修改
    所以要用res.append(path[:]) 浅拷贝，而不是res.append(path) 
    """
#剪枝优化
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtracking(n, k, 1, [], res)
        return res

    def backtracking(self, n, k, startindex, path, res):
        if len(path) == k:
            res.append(path[:])
            return  # 这条路径已经完成，不需要再深入递归了
        for i in range(startindex, n - (k - len(path)) + 2):
            path.append(i)
            self.backtracking(n, k, i + 1, path, res)
            path.pop()
    """
    如果不确定剪枝的范围区间，可以拿极端情况跑一遍 比如n = k = 4
    """
