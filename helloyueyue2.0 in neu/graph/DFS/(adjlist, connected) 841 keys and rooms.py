class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #Figure out whether rooms are all connected
        #DFS: Find and traverse through all the neighbor of the room
        '''
        From GPT:
        I model rooms as a directed graph where rooms[i] is adjacency list of room i.Then I run DFS from room 0 to mark all reachable rooms, and finally check if all rooms are visited.
        '''
        n = len(rooms)
        visited = [False] * n
        def dfs(i):
            if visited[i]:#base case
                return

            # Mark the room as visited
            visited[i] = True

            # Traverse through neighbors
            for neighbor in rooms[i]:
                if not visited[neighbor]:
                    dfs(neighbor)
        dfs(0)
        return visited == [True] * n