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

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        dist_dict = defaultdict(int)
        for i, a in enumerate(alphabet):
            dist_dict[a] = i
        for i, ch in enumerate(s):
            predicted_dist_of_ch = distance[dist_dict[ch]]
            if (not ((predicted_dist_of_ch+1)+i < len(s) and s[(predicted_dist_of_ch+1)+i] == ch)
                    and
                not (i-(predicted_dist_of_ch+1) >= 0 and s[i-(predicted_dist_of_ch+1)] == ch)):
                return False
        return True
        """
     The logic for boolean is: 
    if not match_forward and not match_backward: return False, else return True
        """