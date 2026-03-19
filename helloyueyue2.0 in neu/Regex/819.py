import re#Regular Expression
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        freq = {}
        words = re.findall(r"[a-z]+", paragraph.lower())
        # ['bob', 'hit', 'a', 'ball', 'the', 'hit', 'ball', 'flew', 'far', 'after', 'it', 'was', 'hit']
        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1
        return max(freq, key=freq.get)
        # freq.get把 key 映射为它的 value，告诉 max() 用value比较
    """
    找最大值本身          max(freq.values())
    找最大值对应的 key    max(freq, key = freq.get)
    同时要 key 和 value  k = max(freq, key=freq.get); 
                        return (k, freq[k])
    
    Regular Expression(Regex正则)
    re.findall()
    
    提取单词 [A-Za-z]+
    提取数字 \d+
    """