#time O(1) space O(n)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None
        for x in nums:
            if x == first or x == second or x == third:
                continue
            if first is None or x > first:
                third = second
                second = first
                first = x
            elif second is None or x > second:
                third = second
                second = x
            elif third is None or x > third:
                third = x
        return third if third is not None else first


#time O(nlog(n)) space O(n)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        if len(nums) < 3:
            return nums[0]
        return nums[2]