class Solution: #优解 space O(1) time O(n)
    def largestAltitude(self, gain: List[int]) -> int:
        total = highest = 0
        for num in gain:
            total += num
            highest = max(total, highest)
        return highest

class Solution:#我的解法 unnecessary array space O(n) time O(n)
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        altitudes = [0] * (n + 1)
        for i in range(n):
            altitudes[i + 1] = altitudes[i] + gain[i]
        return max(altitudes)