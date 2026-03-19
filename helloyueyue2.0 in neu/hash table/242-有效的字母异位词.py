#yy思路：将s放入哈希表中，遍历t是否与表对应，每遍历一个删除一个表中的key，最后检查是否是空表
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        for char in t:
            if char not in seen:#不加这句通过不了 比如s = "a", t = "ab",除非加上len(s) == len(t)判断
                return False
            seen[char] -= 1
            if seen[char] == 0:
                del seen[char]
        return len(seen) == 0
    """
    time: O(n)
    space: O(1)仅限26字母，O(n)任意字符
    """