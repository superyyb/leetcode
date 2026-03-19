class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l<=r:
            mid = l + (r - l)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l
    """
在整个循环过程中，始终保持：
    区间	                含义
[0, right]	    所有 < target 的元素
[left, n-1]	    所有 ≥ target 的元素
当循环结束：
right = left - 1
所以：
left = 第一个 ≥ target 的位置
right = 最后一个 < target 的位置
    """
