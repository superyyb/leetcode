#双指针针对sorted array： time O(n) space O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

#如果是无序数组 比如leetcode1，才用hash： time O(n) space O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            if target - num in seen:
                return [seen[target - num]+1, i+1]
            seen[num] = i