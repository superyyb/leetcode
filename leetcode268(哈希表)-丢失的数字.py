#解1：数学解法：len(nums)求和减去数列求和 求得消失的数字
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        res_sum=(1+n)*n/2
        total=sum(nums)
        return int(res_sum-total)

#解2：哈希集合，先全部加入集合，再依次检查少了哪个数字
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        hash={}
        for num in nums:
            if num not in hash:
                hash[num]=1
        for i in range(len(nums)+1):
            if i not in hash:
                return i

#简化版解2
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s=set(nums)
        for i in range(len(nums)+1):
            if i not in s:
                return i