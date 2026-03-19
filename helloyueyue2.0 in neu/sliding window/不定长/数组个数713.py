class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        ans = 0
        n = len(nums)
        for right in range(n):
            product *= nums[right]
            while product >= k and left <= right: #left右移是为了缩小窗口，重新满足条件
                product = product // nums[left]
                left += 1
            ans += right - left + 1
        #“每次向右扩一个点，合法区间也随之改变；最终区间长度即新子数组个数
        return ans