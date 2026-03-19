#给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，
# 满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。

#yy思路：设立一个dict，把nums的index和内容分别设为key和value，双指针法判断num[i]，[j]是否相等
#通过字典记录最近 k 个元素，在遍历列表时检查是否存在重复元素，并且它们的索引差不超过 k。
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numDict=dict()
        for i in range(len(nums)):
            if nums[i] in numDict:
                return True
            numDict[nums[i]]=1
            if len(numDict)>k:#检查字典的长度是否超过了 k。
                del numDict[nums[i-k]]
#如果超过了，说明已经遍历了超过 k 个元素，要将最早加入字典的元素移除。
        return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {} #建立一个哈希表
        for i, num in enumerate(nums): #用enumerate函数将nums转换为索引序列
            if num in pos and i - pos[num] <= k: #需要num相同
#检查当前元素 num 是否已经在字典 pos 中并且当前索引 i 与这个元素上一次出现的索引 pos[num] 之间的差值是否小于或等于 k。
                return True
            pos[num] = i
#如果当前元素 num 不在字典中，或者在字典中但索引差超过了 k，那么将 num 及其当前的索引 i 记录在字典 pos 中。
        return False


