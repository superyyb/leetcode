class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        #和index有关，必须同时记录num和index
        total = len(nums)*(len(nums) - 1)//2
        seen = {}
        good_pairs = 0
        for i, num in enumerate(nums):
            good_pairs += seen.get(num - i, 0)
            seen[num - i] = seen.get(num - i, 0) + 1
        return total - good_pairs
        """
        freq.get(key, 0) 的作用
		当 key 不在字典里时，freq.get(key, 0) 会返回你指定的默认值 0，而不会报 KeyError。
        """