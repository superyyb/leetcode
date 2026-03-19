class MyQueue:

    def __init__(self):
        self.stack_in = [] #push
        self.stack_out = [] #pop

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:#目标是获得queue的头
        ans = self.pop()#调用刚刚定义的pop 逻辑
        self.stack_out.append(ans)
        return ans
    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

"""
pop()：返回队头 + 删除队头。
peek()：返回队头 + 不删除队头。
在 peek() 里调用了 self.pop()，虽然拿到了正确的队头 ans，但这一步已经把它删掉了。为了维持队列不变，需要：
self.stack_out.append(ans)
"""