#time: O(n) (max(), Counter())   space:O(n)(构建Counter())
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        #分清楚情况最重要：k = 1, k = n, 1 < k < n
        freq = Counter(nums)
        if k == 1:
            candidates = [num for num, count in freq.items() if count == 1]
            return max(candidates) if candidates else -1
        if k == len(nums):
            return max(nums)
        #1 < k < n
        if freq[nums[0]] == 1 and freq[nums[-1]] == 1:
            return max(nums[0], nums[-1])
        elif freq[nums[0]] == 1 or freq[nums[-1]] == 1:
            return nums[0] if freq[nums[0]] == 1 else nums[-1]
        else:
            return -1