class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        dict计水果种类，len(dict)>2则窗口不合法，left向右收缩窗口，不可以用set，set一删就删光了
        """
        left = 0
        n = len(fruits)
        seen = {}
        max_ans = ans = 0
        for right, x in enumerate(fruits):
            seen[x] = seen.get(x, 0) + 1 #扩
            while len(seen) > 2: #缩
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del  seen[fruits[left]]
                left += 1
            ans = right - left + 1 #更新
            max_ans = max(max_ans, ans)
        return max_ans