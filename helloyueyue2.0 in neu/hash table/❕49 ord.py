#用count= [0] * 26 每个字符串计数 O(k)，总共 O(n * k)
#Counter()函数更慢，此题用26位数组最优
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Use hashmap to classify strings
        1.Create a hashmap
            Key: Frequency of letters in each string
            Value: String
            If same frequency, add the strings to the value
        2.Return the list of values
        '''
        dic = {}
        for str in strs:
            count = [0] * 26  # 每个str都有一个count
            for char in str:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            if key not in dic:
                dic[key] = []
            dic[key].append(str)  # 后续遇到，直接append
        return list(dic.values())
'''
    list  ❌ 不可 hash → 不能当 dict key
    tuple ✅ 可 hash → 可以当 dict key
    Python 规定：字典的 key must be immutable, tuple can't be changed after created
⚠️字典本身不能append，但是如果字典的value支持append则可以
'''

#❌解
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for str in strs:
            freq = [0] * 26 #Every str has a freq
            for char in str:
                freq[ord(char) - ord('a')] += 1
            freq = tuple(freq)
            if freq not in dic:
                dic[freq] = str#❌value在一开始被设置成了string
                #✅dic[freq] = [str]
            else:
                dic[freq].append(str)#报错： 'str' object has no attribute 'append'
        return list(dic.values())


#用sorted 每个字符串排序 O(k log k)，总共 O(n * k log k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for str in strs:
            key = "".join(sorted(str))#把str排序后作为key
            if key not in dic:
                dic[key] = []
            dic[key].append(str)
        return list(dic.values())

