#yy思路：把nums变成哈希表，对每一个num，查找表中是否有target-num，
#有则return，没有则将其存入表中

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash={} #初始化哈希表
#不用着急把hash表填满，不符合if条件之后再加进去
        for i in range(len(nums)):
            if target-nums[i] in hash:
                return i,hash[target-nums[i]]
            hash[nums[i]]=i
        return[]

'''
hashmap={}
for ind,num in enumerate(nums):
#用enumerate弄出ind和num
    hashmap[num] = ind
缺点：当数组中有重复元素时会覆盖之前存储的索引
 '''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash={}
        for i,num in enumerate(nums):
            hash[num]=i
        for i in range(len(nums)):
            a=target-num
            if a in hash:
                return [i,hash[a]]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash={}
        for i,num in enumerate(nums):
            a=target-nums[i]
            if a in hash:
                return [i,hash[a]]
            hash[num]=i
