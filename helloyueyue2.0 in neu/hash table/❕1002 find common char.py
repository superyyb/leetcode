class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = [float('inf')] * 26

        for word in words:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            for i in range(26):
                freq[i] = min(freq[i], count[i])

        res = []
        for i in range(26):
            res += [chr(i + ord('a'))] * freq[i]

        return res

#用Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words
        res = []
        word1 = set(words[0])
        for char in word1:#直接拿word[0]当作参照物
            frequency = min([word.count(char) for word in words])
            res += [char] * frequency
        return res

#用hash
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        seen = {}
        res = []
        i = 0
        while i < len(words):
            for w in words[i]:
                seen[w] = seen.get(w, 0) + 1
            i += 1
        for key in seen.keys():
            times = min(word.count(key) for word in words)
            while times > 0:
                res.append(key)
                times -= 1
        return res
    """
    遍历seen中所有字符，取每个字符在每个单词里出现的最小次数
    比如l在["bella","label","roller"]里最小次数是2
    """





