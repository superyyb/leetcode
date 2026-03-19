#Jan6复盘
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 如果不剪枝可以不用sort
        res = []
        path = []
        n = len(candidates)
        def backtrack(startIndex, currSum):#当currSum通过参数表达，就别让它成为可变全局状态
            if currSum == target:
                res.append(path[:])
                return
            if currSum > target:
                return
            for i in range(startIndex, n):
                if currSum + candidates[i] > target:
                    break #只有sort之后，剪枝判断才有意义
                path.append(candidates[i])
                backtrack(i, currSum + candidates[i])#用了第 i 个元素，可以重复选i
                path.pop()
        backtrack(0, 0)
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()#如果不剪枝可以不用sort
        path = [] #❗path可以定义在最前面，不用担心答案累积，因为pat通过append + pop每次都恢复
        res = []
        def backtracking(curr_sum, startindex):
            if curr_sum == target:#终止条件有两种：sum>target和sum==target。
                res.append(path[:])
                return# ✅ 找到了一个完整解，不能再继续往下加数了（否则会超过 target）
            if curr_sum > target:
                return
            for i in range(startindex, len(candidates)):
                curr_sum += candidates[i]
                path.append(candidates[i])
                backtracking(curr_sum, i)
#❗(Jan 6继续❌了)允许重复选 因此继续传递i即可，不需要传startindex+1,但是仍然需要startindex保证不回头选之前的元素
                path.pop()
                curr_sum -= candidates[i]
        backtracking(0, 0)
        return res

"""
startindex用途
1，for loop中控制当前层的搜索起点，i 从 start_index 遍历到 len(nums)-1，
避免当前 for 循环回头选
2，backtracking函数中控制下一层的搜索范围，限制下一层只能向后看，防止重复组合

什么时候需要startindex：
如果是一个集合来求组合的话，就需要startIndex，例如：本题，77.组合，216.组合总和III。
如果是多个集合取组合，各个集合之间相互不影响，那么就不用startIndex，例如：17.电话号码的字母组合

for循环中(start_index, len(candidates))，保证不回头选之前的数字
而backtracking(curr_sum, i + 1),保证每个数字在本路径中只能用一次。
"""