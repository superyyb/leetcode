#用count= [0] * 26 每个字符串计数 O(k)，总共 O(n * k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord("a")] += 1 #⚠️ord用法
            key = tuple(count)
            if key not in dic:#第一次遇到，创建[]
                dic[key] = []
            dic[key].append(str)#后续遇到，直接append
        return list(dic.values())
"""
⚠️字典本身不能append，但是如果字典的value支持append则可以
"""
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