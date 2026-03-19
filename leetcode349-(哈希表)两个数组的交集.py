#题目：给定两个数组nums1和nums2求交集。结果中的每个元素是唯一的。不考虑输出结果的顺序
# （时间复杂度太高）yy思路：遍历，重复元素放到一个新的集合中，输出这个集合
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1=set()
        for num in nums1:
            if num in nums2:
                set1.add(num)
        return list(set1)#list和set最简单转换
sol=Solution()
nums1=[1,2,2,1]
nums2=[2,2]
print(sol.intersection(nums1,nums2))

#用哈希表解决降低时间复杂度
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hash={} #初始化哈希表
        res=[]
        if nums1==[] or nums2==[]:
            res=[]
        for i in nums1:
            if not hash.get(i):
                hash[i]=1#去除所有重复的元素，即只保留每个元素的第一次出现
        for j in nums2:
            if hash.get(j):
                res.append(j)
                hash[j]=0
        return res

#回顾解法：
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res_set=set()
        hash1={}
        for i in nums1:
            hash1[i]=1
        for j in nums2:
            if j in hash1:
                res_set.add(j)
        return list(res_set)

