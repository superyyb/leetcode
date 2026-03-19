class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:#至少需要三个元素才能完成三个阶段
            return False
        i = 1
        #设立三个while循环分别代表三个阶段
        while i < n and nums[i - 1] < nums[i]:
                i += 1
        if i == 1: #说明根本没有第一阶段
            return False
        dec_start = i
        while i < n and nums[i - 1] > nums[i]:
            i += 1
        if i == dec_start:
            return False
        inc_start = i
        while i < n and nums[i - 1] < nums[i]:
            i += 1
        if i == inc_start:
            return False
        return i == n#必须走完整个数组

#优秀解法
class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)
        for p in range(1, n - 1):
            if not all(nums[i] < nums[i + 1] for i in range(p)):
                continue
            for q in range(p + 1, n - 1):
                if (all(nums[i] > nums[i + 1] for i in range(p, q))
                    and all(nums[i] < nums[i + 1] for i in range(q, n - 1))):
                    return True
        #如果找到一组满足条件的 (p, q) 就返回 True，否则最终返回 False。
        return False
    """
    all()用法：
    用来判断一个可迭代对象（iterable）中的所有元素是否都为真
    """