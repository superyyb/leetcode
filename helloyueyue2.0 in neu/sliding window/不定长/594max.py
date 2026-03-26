from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for num in count:
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])

        return res

#Sliding window time: O(nlogn) space:O(1)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        nums.sort()#answer is to return the length, so order is not needed
        left = 0#j:left bound
        for right in range(n):#i: right bound, scan through the list
            while nums[right] - nums[left] > 1:#use while to skip multiple invalid numbers
                left += 1 #move right,no longer satisfy with the condition
            if nums[right] - nums[left] == 1:
                count = max(count, right - left + 1)
        return count