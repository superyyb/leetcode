'''
必须从距离终点最近的车开始处理。必须reverse
因为 car fleet 的本质是：
后面的车（pos 小）会不会追上前面的车（pos 大）。
所以顺序必须是：从大位置 → 小位置。
'''
#更好理解一点：当后面一辆车 time > 前面车的 time，append进栈，形成新的车队
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for pos, sp in zip(position, speed):
            cars.append([pos, sp])
        cars.sort(key = lambda x: x[0], reverse = True)
        for pos, sp in cars:
            time = (target - pos)/sp
            while not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []  # store the time every car uses to reach destination
        for pos, speed in zip(position, speed):
            cars.append([pos, speed])
        cars.sort(key=lambda x: x[0], reverse=True)
        for pos, speed in cars:
            time = (target - pos) / speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
