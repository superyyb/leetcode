from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window with unfixed length
        # 遍历s的每个char 如果char在t里面 就算到Counter里面，比较window和template
        # 如果长度刷新最小值，更新res
        # 并尝试缩小窗口。
        '''
        Sliding window(unfixed length)
        1. Use a hashmap to store the freq of t
        2. Use another hashmap as the sliding window
        3. Compare these 2 hashmaps and update the shorthest length and result
        4.Shrink the window
        '''
        template = Counter(t)
        window = Counter()
        left = 0
        res = ''
        have = 0
        need = len(template)#⚠️这里不是len(t)
        shortest_len = float('inf')
        for right, char in enumerate(s):
            if char in template:
                window[char] += 1
                if window[char] == template[char]:
                    # 刚好从不够变得够了，缩进不要写错，对于不在 template 里的字符：window[char]始终是 0
                    have += 1
            while have == need:
                curr_len = right - left + 1
                if curr_len < shortest_len:
                    res = s[left: right + 1]
                    shortest_len = curr_len
                if s[left] in template:
                    window[s[left]] -= 1
                    if window[s[left]] < template[s[left]]:
                        have -= 1
                left += 1
        return res

    '''
    不可以if char in t:
            window[char] += 1 然后判断window == template
    因为很多时候window的字符会多于template
    s = "AAABC"
    t = "ABC"
    '''
