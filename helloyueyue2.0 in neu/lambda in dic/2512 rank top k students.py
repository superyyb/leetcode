# #time O(n * w + n log n)  space: O(n + P + N)
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        n = len(student_id)
        grades = {}
        pos = set(positive_feedback)#在for loop之前把list变set，O(n)降为O(1)
        neg = set(negative_feedback)
        for i in range(n):
            point = 0
            for word in report[i].split():
                if word in pos:
                    point += 3
                elif word in neg:
                    point -= 1
            grades[student_id[i]] = point
        res = sorted(grades.keys(), key=lambda x: (-grades[x], x))#-grades就是按照降序排,先按照-grades[x]排序，再按照x(stu_id)排序
        return res[:k]

#用heap在 k ≪ n 时明显更快
#time O(n·w + n log k)  space: O(k + P + N)
from collections import heapq
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        n = len(student_id)
        heap = []
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        for i in range(n):
            point = 0
            for word in report[i].split():
                if word in pos:
                    point += 3
                elif word in neg:
                    point -= 1
            heapq.heappush(heap, [-point, student_id[i]])
        res = []
        while k:
            grade = heappop(heap)
            res.append(grade[1])
            k -= 1
        return res
