#two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i += 1
            j += 1
        return i == len(s)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = list(s)
        for char in t:
            if queue and queue[0] == char:
                queue.pop(0)
                # If all characters in s have been matched, we can break early.
                if not queue:
                    break
        return len(queue) == 0

=