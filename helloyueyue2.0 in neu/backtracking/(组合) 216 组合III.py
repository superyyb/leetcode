#参数少版本
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(startIndex, curr_sum):
            if curr_sum > n:
                return
            if curr_sum == n and len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex, 9 - (k - len(path)) + 2):
                if curr_sum + i > n:
                    break
                path.append(i)
                backtracking(i + 1, curr_sum + i)
                path.pop()
        backtracking(1, 0)
        return res

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        self.backtracking(k, n, 1, 0, path, res)
        return res
    def backtracking(self, k, n, startindex, curr_sum, path, res):
        if curr_sum == n and len(path) == k:
            res.append(path[:])
            return
        for i in range(startindex, 9 - (k - len(path)) + 2):
            if curr_sum > n: #剪枝
                break
            curr_sum += i
            path.append(i)
            self.backtracking(k, n, i + 1, curr_sum, path, res)
            curr_sum -= i
            path.pop()

    """
    我们需要从数字集合中选出 k 个数：
    backtrack(1, [])  # 第 1 层，从 1 开始
    │
    ├── i = 1 → path = [1] → backtrack(2, [1])  # 第 2 层，从 2 开始
    │   ├── i = 2 → path = [1,2] → backtrack(3, [1,2])  # 第 3 层，从 3 开始
    │   │   └── i = 3 → path = [1,2,3] → 收集结果
    │   └── i = 3 ...
    │
    ├── i = 2 → path = [2] → backtrack(3, [2])
    │   ├── i = 3 ...

•	每一层 for 是在当前“节点”下的所有“子节点”中做选择；
•	每一次 backtrack(i + 1) 是深入下一层，从 下一个数开始，避免重复和回头选；
    """