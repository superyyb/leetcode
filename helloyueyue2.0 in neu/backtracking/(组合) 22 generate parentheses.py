#显式回溯
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        生成原则：
        1.'(': left数量小于n
        2.')': right数量小于left
        """
        stack = []
        res = []
        def backtracking(left, right):
            if left == right == n:
                res.append(''.join(stack))
                return
            if left < n:
                stack.append('(')
                backtracking(left + 1, right)
                stack.pop()
            if right < left:
                stack.append(')')
                backtracking(left, right + 1)
                stack.pop()
        backtracking(0, 0)
        return res

    '''
    这个题之所以不用 for i in range(n)，是因为每一层的“可选集合”不是“从 0..n 里挑东西”
        还能放左括号：如果 left < n，可以放 '('
        还能放右括号：如果 right < left，可以放 ')'
    也就是说，每一步只有最多两个分支，而不是一个固定长度的候选数组需要 for 去枚举。
    '''

#隐式回溯：每次调用 dfs(...)，都把当前字符串 s 的副本传了进去；
#Python 会为这个递归调用创建新的函数栈帧；
#当这个调用结束（return）时，程序会自动回到上一个调用点。
#这一步 —— 从子调用返回父调用，就是「回溯」。
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(left, right, s):
            if len(s) == 2*n:
                res.append(s)
                return
            if left < n:
                backtracking(left + 1, right, s + '(')
            if right < left:
                backtracking(left, right + 1, s + ')')
        backtracking(0, 0, '')
        return res
'''
回溯的本质是：在某个路径走到底后，退回到上一步，继续探索别的分支。
    显式写法：我们用 stack.pop() 把路径手动撤销；
    隐式写法：每次递归时复制 s，返回后 Python 自动丢弃那一层的副本；
所以“回退状态”的效果由函数返回机制隐式完成。
每次函数返回 → 就相当于“撤销了上一步选择”。
'''
