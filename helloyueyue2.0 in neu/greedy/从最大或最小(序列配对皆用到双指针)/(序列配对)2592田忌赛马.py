class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        #田忌赛马 数列排序后，每次把比当前数字大一点的数字比较
        nums.sort()
        i, j = 0, 0#双指针，i指向当前数字，j指向perm对应数字
        while j < len(nums):
            if nums[i] < nums[j]:
                i += 1
            j += 1
        return i

"""
如果不能理解为什么是return i 而不是return i + 1 加上count就比较好理解了
"""
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, 0#双指针，i指向当前数字，j指向perm对应数字
        count = 0
        while j < len(nums):
            if nums[i] < nums[j]:
                i += 1
                count += 1
            j += 1
        return count