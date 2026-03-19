#Mar7复盘
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        temperatures = [73,74,75,71,69,72,76,73]
        output:[1,1,4,2,1,1,0,0]
        stack:
        1.Travsere through the temperatures
        2.Push the index of temperature into stack
        3.Everytime compared with stack[-1]:
            if current temperature > temperatures[stack[-1]]: pop stack[-1], set res[stack[-1]]
        '''
        res = [0] * (len(temperatures))
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res

    """
    单调栈monotonic stacks:元素（通常是索引）按照某个单调性排列：
	•	单调递减栈：栈顶最小 栈底最大。
	•	单调递增栈：栈顶最大,栈底最小。
    为什么存索引而不是值：很多题需要位置；而且能用 arr[i] 取值、比较。
    """

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackIndex, stackT = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((i, t))
        return res

    class Solution:
        def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            stack = []
            res = [0] * len(temperatures)
            for i in range(len(temperatures)):
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    index = stack.pop()
                    res[index] = i - index
                stack.append(i)
            return res
    '''
    把while改成if会发生什么：
        用 if： 只弹一次，只处理一个比当前温度更低的天
    •	用 while： 一直弹，处理一连串比当前温度低的所有天（正确做法）
    '''

    """
    “要找更大，用递减；把比top小的push进去，形成递减栈
    1. 找“右边第一个更大元素”[2, 1, 4]
    •	先 push 2 → [2]
    •	下一个 1：比 2 小，push → [2,1]（递减 ✅）
    •	下一个 4：比 1 大 → 1 出栈；比 2 大 → 2 出栈。
    
    要找更小，用递增。”把比top大的push进去，形成递增栈
    2. 找“右边第一个更小元素”[2, 5, 1]
    •	先 push 2 → [2]
    •	下一个 5：比 2 大，push → [2,5]（递增 ✅）
    •	下一个 1：比 5 小 → 5 出栈；比 2 小 → 2 出栈。
    """