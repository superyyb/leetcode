class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        第三边小于两边之和 [1,2,3,7,8]
        greedy:数列先排序，第三边取数列最大值 另外两边双指针
        """
        n = len(nums)
        nums.sort()
        count = 0
        for k in range(n - 1, 0, -1):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:#滑窗思想
                    count += j - i
                    j -= 1#满足则收缩
                else:
                    i += 1#不满足则扩张
        return count