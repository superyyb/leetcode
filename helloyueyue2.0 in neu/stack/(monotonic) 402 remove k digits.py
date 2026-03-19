class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        nums = list(num)
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(nums[i])
        while k:#注意这的logic
            stack.pop()
            k -= 1
        res = ''.join(stack).lstrip('0')
        return res if res else '0'