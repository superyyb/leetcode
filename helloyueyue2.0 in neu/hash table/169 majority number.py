#最优解：time O(n) space O(1)
#顺序不影响结果，多数元素超过 n/2 的这个性质保证了它永远抵消不完
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        candidate, count = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


#hashmap慢解 time O(nlogn) space O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        values = sorted(freq.items(), key = lambda x:x[1], reverse = True)
        return values[0][0]

#hashmap优化 time O(n) space O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > n / 2:
                return num



