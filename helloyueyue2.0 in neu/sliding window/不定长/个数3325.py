class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        seen = {}
        n = len(s)
        count = 0
        left = 0
        for right in range(n):
            seen[s[right]] = seen.get(s[right], 0) + 1
            while seen[s[right]] >= k:
                count += n - right
                seen[s[left]] -= 1#为什么这里不用考虑seen[s[left]]==0时将其del
                left += 1
        return count

        """
        while seen[s[right]] >= k:无论 seen 里其他字符的计数是不是 0，都 不会影响到 seen[s[right]] >= k 这个判断。
        对比需要删键的场景
	•	在 LC1358、LC2799 里，我们用的是 while len(seen) == 去判断窗口里「到底还剩几种不同字符」，这时 字典里有多少个 key 就直接影响了 len(seen)，所以当某个字符的计数降到 0，就必须 del seen[char]，才能让 len(seen) 真实反映「窗口里不同字符的种类数」
        """