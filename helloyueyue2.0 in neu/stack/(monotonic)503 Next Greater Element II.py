#easier to understand
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums * 2 #circularly
        stack = []
        res = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                res[index] = nums[i]
            if i < len(nums):
                stack.append(i)
        return res[:len(nums)//2]

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #monotonic stack top->down smallest->biggest
        """
        题目要求数组是circularly，因此遍历两遍
        i % n目的是为了让index在[0, n - 1]循环
        nums = [2, 1, 3]
        n = 3
        i:      0  1  2  3  4  5
        i % n:  0  1  2  0  1  2
        但同时我们只需要更新res 的前 n 个位置。
        """
        n = len(nums)
        res = [-1] * n
        stack = [] #stack:只存index就行
        for i in range(2*n):
            curr = nums[i % n]
            while stack and curr > nums[stack[-1]]:
                stackIndex = stack.pop()
                res[stackIndex] = curr#加入res的是从stack里pop出来的，这就是为什么找右边更大的需要递减stack
            if i < n:
                stack.append(i)
        return res