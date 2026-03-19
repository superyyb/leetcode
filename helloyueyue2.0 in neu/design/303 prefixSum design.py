class NumArray:
    def __init__(self, nums: List[int]):
        self.prefixSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefixSum[i + 1] = self.prefixSum[i] + nums[i]
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right + 1] - self.prefixSum[left]

    """
凡是每次调用都一样、可以提前算好的东西，就放在 __init__。
凡是每次调用参数不同、需要实时计算的逻辑，就放在方法里。
    
    任意子数组的和，都可以表示为两个前缀和的差
    下标区间 [left,right] 的元素和等于前缀 [0,right] 的元素和
    减去另一个前缀 [0,left−1] 的元素和，即s[right+1]−s[left]
    """

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums#成员变量，需要在不同方法里用
    def sumRange(self, left: int, right: int) -> int:
        total = 0#局部变量 用完就结束
        for i in range(left, right + 1):
            total += self.nums[i]
        return total

"""
•	想清楚我需要哪些操作，每个操作需要哪些数据」；
•	在 __init__ 里定义能支撑这些操作的数据结构；
•	在方法里使用这些变量完成操作。
"""