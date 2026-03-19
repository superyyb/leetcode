#我的解法：
 #1.candidates.remove(curr[i]) candidates.append(curr[i])非常没必要
 #2.没有bank转为list
 #3.不需要存 neighbors 列表，其实可以边生成边判断边入队
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''
        BFS: find shortest path
        1.graph: from startGene to endGene
        2.Only genes in bank are regarded as valid step
        3.Neighbors: Every gene has 32 neighbors(choices from 'A', 'C', 'G', and 'T')
        4.Cound the step while traversing
        5.Edge cases: visited, not in bank
        '''
        if endGene not in bank:
            return -1
        if startGene == endGene:
            return 0
        q = deque([(startGene, 0)])
        visited = set()
        visited.add(startGene)
        candidates = ['A', 'C', 'G', 'T']
        while q:
            curr, step = q.popleft()
            if curr == endGene:
                return step
            neighbors = []
            for i in range(8):  # "AACCGGTT"
                candidates.remove(curr[i])
                for candidate in candidates:
                    neighbors.append(curr[:i] + candidate + curr[i + 1:])
                candidates.append(curr[i])
            for nei in neighbors:
                if nei in visited or nei not in bank:
                    continue
                q.append((nei, step + 1))
                visited.add(nei)
        return -1

#优解
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''
        BFS: find shortest path
        1.graph: from startGene to endGene
        2.Only genes in bank are regarded as valid step
        3.Neighbors: Every gene has 32 neighbors(choices from 'A', 'C', 'G', and 'T')
        4.Cound the step while traversing
        5.Edge cases: visited, not in bank
        '''
        bank = set(bank)
        if endGene not in bank:
            return -1
        if startGene == endGene:
            return 0
        q = deque([(startGene, 0)])
        visited = set()
        visited.add(startGene)
        while q:
            curr, step = q.popleft()
            if curr == endGene:
                return step
            neighbors = []
            for i in range(8):#"AACCGGTT"
                for ch in "ACGT":
                    if ch == curr[i]:
                        continue
                    nei = curr[:i] + ch + curr[i+1:]
                    if nei in visited or nei not in bank:
                        continue
                    q.append((nei, step + 1))
                    visited.add(nei)
        return -1



