class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        subarray = []
        #used = set()❌把used定义为全局变量，一旦某个数字在某层出现过，它在所有其他层都不能用了
        def backtracking(startIndex):
            used = set()#✅每一层新建一个used
            if len(subarray) >= 2:
                res.append(subarray[:])#收集答案不需要return，继续往下还有更多子集可以枚举
            for i in range(startIndex, len(nums)):
                if (subarray and nums[i] < subarray[-1]) or nums[i] in used:
                    continue
                subarray.append(nums[i])
                used.add(nums[i])
                backtracking(i + 1)
                subarray.pop()
        backtracking(0)
        return res
    """
if i > startIndex and nums[i] == nums[i - 1]:不再适用本题，
因为这次nums不可以sort，只能用一个set去重

学习如何保证非递减，if (subarray and nums[i] < subarray[-1])
不要再用蠢蠢的subarray == sorted(subarray)了！！
    """

"""
子集问题对比组合问题：
什么时候收集答案之后要加return：
-》是否要 return，取决于问题是不是“构造一个满足条件的终点路径”
还是“枚举所有可能的路径”。

"""
