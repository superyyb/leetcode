#BFS 之所以逐层遍历，在代码中体现在使用 deque 和 popleft() 的操作上，
# 队列保证了先进先出（FIFO），从而层层扩展。
from collections import deque
def BFS(graph,start,goal,path=None):
    if path==None:
        path=[start]
        queue=deque([(start,path)])
    visited=set()
    while queue:
        node,path=queue.popleft()
        if node==goal:
            return path
        for neighbor in graph.get(node,[]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,path+[neighbor]))
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
if __name__=="__main__":
    print(BFS(graph,start="A",goal="F"))

