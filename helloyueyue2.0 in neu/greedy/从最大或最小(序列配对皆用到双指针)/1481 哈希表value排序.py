class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        counts = sorted(freq.values())
        for i in range(len(counts)):
            if k >= counts[i]:
                k -= counts[i]
            else:
                return len(counts) - i
        return 0 #别漏了如果k一直大于等于所有频次之和的情况