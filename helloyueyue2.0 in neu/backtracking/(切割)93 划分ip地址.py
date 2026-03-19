#另写函数判断是否合法（<255，没有leading 0...）
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        def backtracking(startIndex, segments):
            if segments > 4:
                return
            if startIndex == len(s) and segments == 4:#只有恰好 4 段且消耗完所有字符才是合法结果。
                res.append(".".join(path))
                #用 "." 把 path 中的字符串连接起来。连接符 . 只会出现在元素之间，而不会出现在开头或结尾
                return
            for i in range(startIndex, min(startIndex+3, len(s))):#优化，最多取三位数
                if isvalid(s[startIndex : i + 1]):
                    path.append(s[startIndex : i + 1])
                    segments += 1
                    backtracking(i + 1, segments)
                    path.pop()
                    segments -= 1
        def isvalid(s):
            if int(s) > 255 or (len(s) > 1 and s[0] == "0"):
                return False
            return True
        backtracking(0, 0)
        return res
"""
为什么这里不用path[:]
    ".".join(path) 本身就创建了一个新的字符串对象，它与 path 的引用没关系：
	•join() 会把 path 中当前的字符串按 “.” 拼成一个新的字符串。
	•这个新字符串是值拷贝，是 immutable，不会受 path.pop() 影响。
"""

#或者segments在函数里加减 就不用回溯了
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        def isvalid(s):
            if int(s) > 255 or (len(s) > 1 and s[0] == "0"):
                return False
            return True
        def backtracking(startIndex, segments):
            if segments > 4:
                return
            if startIndex == len(s) and segments == 4:
                res.append(".".join(path))
                return
            for i in range(startIndex, min(startIndex + 3, len(s))):
                if isvalid(s[startIndex: i + 1]):
                    path.append(s[startIndex: i + 1])
                    backtracking(i + 1, segments + 1)
                    path.pop()
        backtracking(0, 0)
        return res