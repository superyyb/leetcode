#	DFS 使用的是栈和 pop()（后进先出，LIFO），
#	导致搜索深入一条路径直到底部，然后回溯，不保证最短路径
def DFS(graph,start,goal,path=None):
    if path is None:
        path=[start]
    visited=set()
    stack=[(start,path)]#use a tuple to trace current node and path
    while stack:
        node,path=stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node==goal:
            return path
        for neighbor in reversed(graph.get(node,[])):
            if neighbor not in visited:
                stack.append((neighbor,path+[neighbor]))
    return None

"""
def DFS(graph,start,goal,path=None,visited=None):
    if path is None:
        path=[start]
    else:
        path=path+[start]
    if visited is None:
        visited=set()
    visited.add(start)
    if start==goal:
        return path
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            new_path=DFS(graph,node,goal,path,visited)
            if new_path is not None:
                return new_path
    return None


        A
       / \
      B   C
     / \   \
    D   E ——F
"""
# unweighted graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
if __name__=="__main__":
    print(DFS(graph,start="A",goal="F",path=None))#,visited=None))

