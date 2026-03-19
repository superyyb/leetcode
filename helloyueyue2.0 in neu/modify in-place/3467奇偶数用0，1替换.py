class Solution: #分别替换了0，1后，用内置函数sorted
    def transformArray(self, nums: List[int]) -> List[int]:
        i, j = 0, 0
        while i < len(nums):
            if nums[i]%2 == 0:
                nums[i] = 0
            else:
                nums[i] =1
            i += 1
        return sorted(nums)

class Solution: #把偶数都移到前面变成0后，后面用1补齐
    def transformArray(self, nums: List[int]) -> List[int]:
        i, j = 0, 0
        while i < len(nums):
            if nums[i]%2 == 0:
                nums[j] = nums[i] = 0
                j += 1
            i += 1
        for i in range(j,len(nums)):
            nums[i] = 1
        return nums