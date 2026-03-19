class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        freq = sorted(freq.items(), key = lambda kv: (kv[1], -kv[0]))
        """
    first sort by frequency(value), if the frequency of the words is same, then sort by key in decreasing order.
    nums = [2,3,1,3,2]
    freq = {1: 2, 2: 3, 3: 1}
    sorted freq = [(3, 1), (1, 2), (2, 3)]
    """
        res = []
        for key, value in freq:
            res += [key] * value
        return res