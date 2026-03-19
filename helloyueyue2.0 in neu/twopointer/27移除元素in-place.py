#Time: O(n) Space: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #双指针：i遍历列表，j负责把不等于 val 的数放到前面
        i, j = 0, 0
        while i <= len(nums) - 1:
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j

