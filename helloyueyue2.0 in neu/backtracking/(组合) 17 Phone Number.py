#显式回溯
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or digits == "1":
            return []
        dic = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}#建立映射
        res = []
        path = []
        def backtracking(index):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            letters = dic[digits[index]]
            for letter in letters:
                path.append(letter)
                backtracking(index + 1)
                path.pop()
        backtracking(0)
        return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        list_digits = list(digits)
        res = []
        path = []
        n = len(digits)
        dic = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}#建立映射
        def backtracking(index):#这里的index是目前正在处理digits第几个数字
            if index == n:#所以也可以这么写
                res.append(''.join(path))
                return
            letters = dic[digits[index]]
            for letter in letters:
                path.append(letter)
                backtracking(index + 1)
                path.pop()
        backtracking(0)
        return res

#隐式回溯,传参path
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or digits == "1":
            return []
        dic = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}#建立映射
        res = []
        path = ""
        def backtracking(digits, index, path, res):
            if len(path) == len(digits):
                res.append(path)
                return
            letters = dic[digits[index]]#先写出逻辑，再用递归实现index+1
            for letter in letters:
                backtracking(digits, index + 1, path + letter, res)
        backtracking(digits, 0, path, res)
        return res
    """
    index 表示的是当前处理的是 digits 字符串中的第几个数字。
    它的值是 0、1、2…，表示“我现在处理第几位数字”。
    而每一位数字（比如 digits[0] = "2") 会对应多个可能的字母（比如 "abc"），这些字母会通过 for letter in letters: 被依次遍历。
    
    为什么没有显式回溯：
    字符串在 Python 中是不可变类型，path + letter 是新建一个字符串，
    前一层的 path 完全不受影响，所以不需要 pop，如果是列表则需要回溯
    """

#隐式回溯,path作为外部变量
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        path = ""
        if not digits or digits == "1":
            return []
        def backtracking(index):
            nonlocal path  #告诉Python我们要修改外层的path
            if len(path) == len(digits):
                res.append(path)
                return
            letters = dic[digits[index]]
            for letter in letters:
                path += letter
                backtracking(index + 1)
                path = path[:-1]#对于immutable字符串，只可以s+=，不可以s-=，回撤要用切片
        backtracking(0)
        return res