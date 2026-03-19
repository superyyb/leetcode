from collections import deque
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> \
    List[str]:
        '''
        BFS:
        1.Start from id, find the level of friends
        2.Get corresponding videos, put them into hashmap
          Key: video, value: freq
        3.Sort the hashmap by value, return the list of videos
        '''
        q = deque([id])
        visited = [0] * len(friends)
        curr_level = 0
        visited[id] = 1
        while q and curr_level < level:  # 没有加level判断条件
            for i in range(len(q)):  # 没有写for loop区分level
                index = q.popleft()
                visited[index] = 1  # 放错位置，出队的时候才置1
                for nei in friends[index]:
                    if visited[nei] == 0:
                        visited[nei] = 1
                        q.append(nei)
            curr_level += 1
        freq = {}
        for friend in q:
            for video in watchedVideos[friend]:
                if video not in freq:
                    freq[video] = 1
                else:
                    freq[video] += 1
        sorted_freq = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        return [key for key, value in sorted_freq]
