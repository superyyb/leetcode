#Jan6复盘
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        n = len(candidates)
        def backtrack(startIndex, currSum):
            if currSum == target:
                res.append(path[:])
                return
            if currSum > target:
                return
            for i in range(startIndex, n):
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue#同一层去重❌又写成i > 0了
                if currSum + candidates[i] > target:#剪枝（可选）
                    break
                path.append(candidates[i])
                backtrack(i + 1, currSum + candidates[i])#用了第 i 个元素，下一层只能从 i 后面继续选
                path.pop()
        backtrack(0, 0)
        return res


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()#⚠️必须先排序：去重依赖相邻相等
        path = []
        res = []
        def backtracking(startIndex, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(path[:])
                return# ✅ 找到了一个完整解，不能再继续往下加数了（否则会超过 target）
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    #⚠️这里必须从本层起点startIndex开始而不是i>0
                    #i > startIndex禁止“在同一层用第二个相同数当起点”
                    #而[1,1,6]当到第二个1的时候 i=startIndex=1不会进入这个if判断
                    continue
                curr_sum += candidates[i]
                if curr_sum > target:#⚠️剪枝
                    break
                path.append(candidates[i])
                backtracking(i + 1, curr_sum)#这里的i+1规定了下一层从 i + 1 开始选，并且更新了下一层的起点startIndex
                path.pop()
                curr_sum -= candidates[i]
        backtracking(0, 0)
        return res
    """
1.回溯中的“同一层”到底是什么？在回溯中，每一层是一个函数调用中的 for 循环。
    这个 for i in range(...) 就是“这一层”横向的所有尝试。
2.为什么要去重：每一层只能尝试一组值中独一无二的数字，一旦你在这一层用过了 2，那其他的 2 就没资格再试了
3.比如我已经选到了[1,2,2]之后，我pop掉第三层的2重新进入第二层，这个时候就该跳过第二层后面两个重复的2 
    """

"""
把 curr_sum + candidates[i] 直接作为参数传入递归，你就只用处理 path 回溯，
不需要处理 curr_sum -= candidates[i]，因为：
递归函数每次调用，curr_sum 是一个新的局部变量，不会影响上一层的 curr_sum。
"""
