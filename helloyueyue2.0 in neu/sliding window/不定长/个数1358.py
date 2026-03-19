class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #用dict记录出现次数
        n = len(s)
        seen = {}
        count = 0
        left = 0
        for right in range(n):
            if s[right] not in seen:
                seen[s[right]] = 1
            else:
                seen[s[right]] += 1
            while len(seen) == 3: #wrong原因：这里一定用的是while
                count += n - right #区别于大部分题的right - left + 1
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
        return count

        """
        当窗口 [left…right] 第一次满足包含 'a','b','c' 时，以这个left为起点、
        任何以end∈[right…n-1]为终点的子串，都会包含这三个字符。
	    这样，从 right 到 n-1 一共有n - right种不同的结束位置，
        因此对这个 left，就能一次性累加 n-right 个合法子串。

        count += right - left + 1：是固定右端点，枚举可行的各个起点
        count += n - right：是固定起点，枚举可行的各个终点
        虽然都是滑动窗口，但你要看题目问“固定哪一端来枚举另一端”，再决定加的是 right-left+1 还是 n-right。
        """