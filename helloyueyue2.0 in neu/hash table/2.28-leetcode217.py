class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s=set()
        for i in range(len(nums)):
            s.add(nums[i])
        return len(s)<len(nums)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
       hash={}
       for num in nums:
            if num in hash:
                return True
            else:
                hash[num]=1
       return False

sol=Solution()
num=[1,2,3,3]
print(sol.containsDuplicate(num))
