class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        count = list(freq.values())
        return len(count) == len(set(count))
