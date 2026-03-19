#yy思路：用enumerate函数写出带下标的list1，把list2放入哈希表。遍历list1找到与哈希表
#中重复的，算出索引总和并取min return
class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        numlist=[] #需要一个numlist存储最后要输出的餐厅
        elist1=enumerate(list1)
        hash={}
        for i,item in elist1:
            hash[item]=i
        min_sum = float('inf')# 初始化最小索引和为一个很大的值
        for index,e in enumerate(list2):
            if e in hash:
                res_sum=index+hash[e]
                if res_sum<min_sum:
                    min_sum=res_sum
                    numlist=[e] #只在numlist保留当前餐厅，随时覆盖
                elif res_sum==min_sum:
                    numlist.append(e)
        return numlist

'''
优化:如果 list1 特别大，而 list2 特别小，那么，就会占用非常多的空间，
所以，考虑只保存长度更小的那个到哈希表。
'''
