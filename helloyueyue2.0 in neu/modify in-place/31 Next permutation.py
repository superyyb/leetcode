class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2#找到降序排列的节点
        while i >= 0 and nums[i] >= nums[i + 1]:#如果是降序排列
            i -= 1
        if i >= 0:# 2) 从右侧找第一个 > nums[i] 的 j
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]#交换
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1