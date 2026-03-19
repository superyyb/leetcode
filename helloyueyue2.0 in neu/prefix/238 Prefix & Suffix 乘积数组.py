#前缀后缀积
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = suffix[n - 1] = 1
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):#从n-2开始，逐步递减到0，包含0，但不包含-1。
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res

#前缀后缀积：不定义数组
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

#繁琐⚠️num为0的情况 分类讨论计算
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        product, zero_count = 1, 0
        for num in nums:
            if num:
                product *= num
            else:
                zero_count += 1
            if zero_count > 1:
                return [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                res[i] = product
            elif zero_count == 0:
                res[i] =  int(product / nums[i])
            else:
                res[i] = 0
        return res