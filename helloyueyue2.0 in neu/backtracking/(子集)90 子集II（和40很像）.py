class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#去重之前需要先对集合排序
        res = []
        subset = []
        def backtracking(startIndex):
            res.append(subset[:])
            # if startIndex >= len(nums):
            #     return k 可以不用写
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue#⚠️又犯了一次错误❌，i > startIndex不是i > 0
                subset.append(nums[i])
                backtracking(i + 1)
                subset.pop()
        backtracking(0)
        return res

#用set解，也必须sorted，例如[2,1,2]如果不sort就会出现重复解([1,2],[2,1])
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        def backtracking(startIndex):
            used = set()
            res.append(path[:])
            for i in range(startIndex, len(nums)):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                backtracking(i + 1)
                path.pop()
        backtracking(0)
        return res