class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list_t=[]
        if s is None:
            return t
        for item in t:
            list_t.append(item)#Building list_t takes O(n) time.
        for item in s:
            if item in list_t:
                list_t.remove(item)
#For each character in s, the check if item in list_t is O(n) in the worst case,
# and list_t.remove(item) is also O(n) in the worst case.
        return list_t.pop()

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_map = {}
        for char in t:#	Building the dictionary from t takes O(n) time.
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        for char in s:#Looping through s takes O(n) time.
            hash_map[char] -= 1

        for char in hash_map:
            if hash_map[char] == 1:
                return char# Find the character with count 1
"""
Which One Is Better?
Time: The dictionary method runs in O(n) time, whereas the list removal method 
may take O(n^2) in the worst case.
Space: Both approaches use O(n) space, although the dictionary often uses 
much less space 
if the set of characters is limited.
"""
if __name__=="__main__":
    sol=Solution()
    s = "abcd"
    t = "abcde"
    print(sol.findTheDifference(s,t))


