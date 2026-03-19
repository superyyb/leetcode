#yy思路：用count找到每个元素出现次数，对应出value为1的元素
from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        countNums=Counter(nums)
        for num,count in countNums.items():#别漏了.items()
            if count==1:
                return num

#回顾解法：
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hash={}
        for num in nums:
            if num in hash:
                hash[num]+=1
            else:
                hash[num]=1
        for key in hash:
            if hash[key]==1:
                return key