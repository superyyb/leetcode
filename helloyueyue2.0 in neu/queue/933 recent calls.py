class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        while self.queue and t - 3000 > self.queue[0]:
            self.queue.pop(0)
        self.queue.append(t)
        return len(self.queue)


'''
Queue 是 FIFO → 理论上应该从 队头删除，从 队尾加入
Stack 是 LIFO → 理论上从 栈顶删除，从 栈顶加入
但是我们用python的list模拟过程，模拟stack:pop() 模拟queue:pop(0)
'''