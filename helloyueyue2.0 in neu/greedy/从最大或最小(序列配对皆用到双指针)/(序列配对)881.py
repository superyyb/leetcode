#我的解法（啰嗦）
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        i, j = 0, len(people) - 1
        while i <= j:
            if people[j] == limit:
                count += 1
            elif people[j] + people[i] <= limit:
                count += 1
                i += 1
            else:
                count += 1
            j -= 1
        return count
    """
    纠结while条件到底是i <= j:还是i < j: 
    不如想想极端情况 people = [3] limit = 3
    """

#简洁写法
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        i, j = 0, len(people) - 1
        while i <= j:
            if people[j] + people[i] <= limit:
                i += 1
            j -= 1
            count += 1
        return count