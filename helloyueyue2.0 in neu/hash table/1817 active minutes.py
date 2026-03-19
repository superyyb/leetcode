#time O(n) space O(n)
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0] * k
        freq = {}
        for id, time in logs:
            if id not in freq:
                freq[id] = set()#⚠️用set作为value
            freq[id].add(time)
        #freq: {0: {2, 5}, 1: {2, 3}}
        for times in freq.values():
            uam = len(times)
            answer[uam - 1] += 1
        return answer