class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        #每个学生找离得最近的座位
        seats.sort()
        students.sort()
        total = 0
        for i in range(len(seats)):
            total += abs(seats[i] - students[i])
        return total