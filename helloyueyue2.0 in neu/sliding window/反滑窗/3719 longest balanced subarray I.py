#time O(n2) space O(n)
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_length = 0
        for i in range(len(nums)):
            odd = set()
            even = set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                if len(even) == len(odd):
                    max_length = max(max_length, j - i + 1)
        return max_length
    """
    为什么不可以sliding window：
    滑窗策略： “while 不等就收缩,需要具备一定单调性才可以用滑窗
     nums = [2, 4, 1, 3]，窗口[2]，此时even = 1 odd = 0
     如果你用while len(even) != len(odd): left += 1,最终什么都得不到
     可是理想答案是[2, 4, 1, 3] = 4
    """