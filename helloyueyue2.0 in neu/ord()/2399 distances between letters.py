#time:O(n) space:O(1) 最多存26个字母
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        #use a dictionary to store the letter and its corresponding distance
        dic = {}
        for i, letter in enumerate(s):
            if letter not in dic:
                dic[letter] = i
            else:
                dic[letter] = i - dic[letter] - 1
    #transfer letter to number("A"->0, "B"->1...)
        for key, value in dic.items():
            index = ord(key) - ord("a")
            if distance[index] != value:
                return False
        return True