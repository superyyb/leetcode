#yy思路：把str enumerate，字母挨个放入哈希表，如果已经存在，key变成2
#写出第一个key为1的value，返回他的索引
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash={}
        for index,item in enumerate(s):
            if item not in hash:
                hash[item] = [index]  # 如果是第一次出现，用一个列表来初始化
            else:
                hash[item].append(index)  # 如果已经存在，追加新的索引到列表
        for key,value in hash.items():
            if len(value)==1:#检查列表长度是否为1
                return value[0] #返回该字符的索引：即列表中的第一位
        return -1
'''
假设字符串为 "leetcode"，处理后 hash 字典如下：
    'l': [0],
    'e': [1, 7],
    't': [2],
    'c': [3],
    'o': [4],
    'd': [5]
'''

#解法2：换一种形式的字典
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]+=1
            else:
                dict[s[i]]=1
        for i in range(len(s)):
            if s[i] in dict and dict[s[i]]==1:
                return i
        return -1 #不用加else也可以
'''
假设字符串为 "leetcode"，处理后 hash 字典如下：
    'l':1,
    'e':3,
    't':1,
    'c':1,
    'o':1,
    'd':1
'''
#用counter函数

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