class Solclass Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        Sort the nums to avoid duplicates
        Use backtracking to generate permutations
        '''
        nums.sort()
        res = []
        path = []
        def backtrack(used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                #❌这个条件没写对，漏了not used[i - 1]
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(used)
# 先把这一条分支往下走完，会继续往下选第二个数、第三个数……在这期间，used[i] 一直是 True，不会撤销。
                path.pop()
                used[i] = False# 回来之后才撤销
        backtrack([False] * len(nums))
        return res

    '''
✅ 场景 A：used[i-1] == False（同层重复起点）
前一个相同数没在当前 path 用过
说明你在“同一层”里想用第二个相同数开新分支
这会产生重复排列
👉 必须 continue
✅ 场景 B：used[i-1] == True（同枝合法使用第二份拷贝）
前一个相同数已经在 path 里了
说明你在“同一条排列”里需要用第二个相同数
👉 必须允许，不要 continue
    '''