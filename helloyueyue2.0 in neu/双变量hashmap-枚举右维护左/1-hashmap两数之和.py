#Mar7 复盘
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        hashmap
        key:num value:index
        Traverse through list: check whether target - num in hashmap, if it is, return answer
        '''
        mapping = {}
        for i, num in enumerate(nums):
            if target - num in mapping:
                return [mapping[target - num], i]
            mapping[num] = i

#yy思路：把nums变成哈希表，对每一个num，查找表中是否有target-num，
#有则return，没有则将其存入表中
#不用着急把hash表填满，不符合if条件之后再加进去
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use hashmap to store the num and index
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [i, hashmap[target - num]]
            hashmap[num] = i

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
