class Solution:#in-place
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        #index starts from 0, so the order is even-odd-even.......
        i, j = 0, 1 #i放偶数位，j放奇数位
        while i < len(nums) and j < len(nums):
            if nums[i]%2 == 0:
                i += 2
            elif nums[j]%2 == 1:
                j +=2
            else: #else代表当nums[i]和nums[j]都在错误位置上时
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        return nums

class Solution:#❌
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i]%2 == 0:
                res[i] = nums[i]
                i += 2
            elif nums[j]%2 == 1:
                res[j] = nums[j]
                j += 2
#错误原因：假设 nums[i]是偶数位置的正确元素，nums[j]是奇数位置的正确元素，会漏掉不在正确位置上的元素

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        i, j = 0, 1
        for num in nums:
            if num%2 == 0:
                res[i] = num
                i += 2
            else:
                res[j] = num
                j += 2
        return res