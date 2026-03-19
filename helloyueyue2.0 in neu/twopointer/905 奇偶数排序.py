#time O(n)  space O(1) in-place
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #双指针 i遍历 j把偶数挪前面
        i, j = 0, 0
        while i < len(nums):
            if nums[i]%2 == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            i += 1
        return nums