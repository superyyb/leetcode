from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        the min total number: BFS to find shortest path
        1. The graph has maximum 10000 cells(from '0000' -> '9999')
        2. Find the neighbor(eg:'0000' has 8 neighbors: '0001', '0009'...)
        3. Use BFS to find the
        4. Edge case: visited, deadends
        '''
        deadends = set(deadends)
        if target in deadends or '0000' in deadends:  # 漏了'0000'是deadend的情况
            return -1
        q = deque([('0000', 0)])  # Append a tuple must use deque([])
        visited = set()
        visited.add('0000')
        while q:
            curr, step = q.popleft()
            if curr == target:
                return step
            neighbors = []
            # How to construct neighbors
            for i in range(4):
                digit = int(curr[i])
                # +1
                up = (digit + 1) % 10
                neighbors.append(curr[:i] + str(up) + curr[i + 1:])
                # -1
                down = (digit - 1) % 10
                neighbors.append(curr[:i] + str(down) + curr[i + 1:])
            for nei in neighbors:
                if nei in deadends or nei in visited:
                    continue
                q.append((nei, step + 1))
                visited.add(nei)
        return -1

'''
之前写法：popleft 后 visited.add(curr)，这也能跑，但会导致同一节点可能被多次入队（浪费）。
更好的写法是：入队时标记 visited（保证每个状态最多入队一次）
'''


