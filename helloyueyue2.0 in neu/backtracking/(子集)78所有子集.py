#求子集问题不需要剪枝优化，因为就是要遍历整个树
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Backtrack
        1.Need to skip the duplicates in the same layer [1,1,2,3]
        '''
        res = [[]]#⚠️记得首先放入[]
        path = []
        def backtrack(startIndex):
            if len(path) > len(nums):
                return#可以省略，因为当startIndex >= len(nums)已经退出for loop
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])#只有在每一次递归“进入节点”时就立即保存路径，才能完整保留所有子集。
                res.append(path[:])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res
