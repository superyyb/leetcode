#方法1:⚠️传参used
# 用used数组存储用过的元素下标（适用性更广，可用于会重复的元素）
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtracking(used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking(used)
                used[i] = False
                path.pop()
        backtracking([False]*(len(nums)))
        return res

#方法2:和方法1本质一样
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = [0] * len(nums)
        def backtracking():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):#从0开始每次都是全局扫
                if used[i]:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtracking()
                path.pop()
                used[i] = 0#为什么这个也要回溯
        backtracking()
        return res
    """
    比如nums = [1, 2]
    拿到[1, 2]这个组合之后如果不回溯，
    那么1，2永远是used[i] = 1
    永远被占用 得不到[2,1]这个组合
    """

#方法3不推荐 都给我整看不懂了 建议别看 用used数组存储用过的元素
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtracking(used, nums):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in used:
                    path.append(nums[i])
                    used.append(nums[i])
                    backtracking(used, nums)
                    path.pop()
                    del used[-1]
        backtracking([], nums)
        return res