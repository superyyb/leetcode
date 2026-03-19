#python得哈希表就是字典？
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numDict=dict()
        for num in nums:
            if num in numDict:
                return True
            else:
                numDict[num]=num#往字典里添加元素
        return False

#解2：用集合去重，比较长度
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numSet=set()
        for num in nums:
            numSet.add(num)
        if len(numSet)==len(nums):
            return False
        else:
            return True

#回顾练习：
#yy思路：把数组存入哈希表，如果出现第二个，return true
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
       hash={}
       for num in nums:
            if num in hash:
                return True
            else:
                hash[num]=1
       return False