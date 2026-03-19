"""
闭区间 (l <= r)：更新左右指针时往往要排除掉 mid，因此可能丢掉最小值，需要额外判断“突变点”。
半开式 (l < r)：不断缩小区间，直到最后只剩下一个元素l == r。那一定是最小值。
            收缩区间时能保证 最小值始终留在搜索范围内，不需要特判突变点。
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if  mid > 0 and nums[mid-1] > nums[mid]:#mid > 0防止mid越界
                return nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:# 最小值一定在右半边
                l = mid + 1
            else:#最小值在左半边，可能就是 mid，不能排除mid
                r = mid
        return nums[l]