#方法1
"""
min_stack 必须和 stack 保持一一对应的长度。
stack[i] 存的是第 i 个元素。
min_stack[i] 存的是“前 i 个元素里的最小值”。
所以两个必须同步 push / pop。
比如：stack = [0,1,1,1,1]
 min_stack = [0,0,0,0,0]
"""
class MinStack:
#因为这道题要记录最小值 而且要O(1)time，再找一个stack记录min
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:#一定要先判断min_stack是否为空，否则min_stack[-1]会报错
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        if not self.stack:
            return None
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return None
        return self.min_stack[-1]

#方法2
"""
min_stack 只存必要的元素，占用空间更小。
比如push [3, 5, 2, 2, 4] → min_stack=[3,2,2]
所以在pop 上个方法min_stack一定保持同步pop 
但是在这个方法min_stack只在pop值刚好等于min_stack[-1]时pop
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None
        val = self.stack.pop()
        if val == self.min_stack[-1]: # 如果要pop的值刚好等于min_stack栈顶
            self.min_stack.pop()
        return val

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return 0
        return self.min_stack[-1]
