class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """
        不定长max：扩，缩，更新答案
        分别计算T和F的出现次数
        """
        left = 0
        count_T = count_F = 0
        max_ans = ans = 0
        n = len(answerKey)
        for right in range(n):
            if answerKey[right] == "T":
                count_T += 1
            else:
                count_F += 1
            while count_T > k and count_F > k:
                #「需要翻转的字符数」超过 k 时，才移动 left。
                if answerKey[left] == "T":
                    count_T -= 1
                else:
                    count_F -= 1
                left += 1
            ans = right - left + 1 #更新答案
            max_ans = max(max_ans, ans)
        return max_ans