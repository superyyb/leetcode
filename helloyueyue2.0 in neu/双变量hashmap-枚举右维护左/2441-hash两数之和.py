class Solution: #hash
    def findMaxK(self, nums: List[int]) -> int:
        #找到list中相加为0的数组中绝对值最大的那个值
        seen = {}
        max_val = -1
        for i, num in enumerate(nums):
            if 0 - num in seen:
                max_val = max(abs(num), max_val)
            else:
                seen[num] = i
        return max_val

class Solution: #set 优点：对于这道题来说不用记录index
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        max_val = -1
        for num in nums:
            if -num in seen:
                max_val = max(abs(num), max_val)
            else:
                seen.add(num)
        return max_val