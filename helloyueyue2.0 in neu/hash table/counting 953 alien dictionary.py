class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        for i, char in enumerate(list(order)):
            alphabet[char] = i
        def compareTwoWords(word1, word2):
            min_len = min(len(word1), len(word2))
            for j in range(min_len):
                if alphabet[word1[j]] < alphabet[word2[j]]:
                    return True#只要第一个满足 直接return True
                elif alphabet[word1[j]] > alphabet[word2[j]]:
                    return False
            return len(word1) <= len(word2)#前缀全部都相同，比较长度
        i = 0
        while i < len(words) - 1:
            if  not compareTwoWords(words[i], words[i + 1]):
                return False
            i += 1
        return True