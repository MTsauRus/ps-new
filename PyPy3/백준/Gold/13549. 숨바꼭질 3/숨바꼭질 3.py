### 숨바꼭질 3
### 다익스트라, bfs
import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
visited = [False for _ in range(200001)]
dist = [float('inf') for _ in range(200001)]

def bfs(a, b):
    queue = deque([a])
    visited[a] = True
    dist[a] = 0
    while queue:
        now = queue.popleft()
        
        next1 = now + 1
        next2 = now - 1
        next3 = now * 2
                    
        if not visited[next3] and 0 <= next3 <= 100000:
            visited[next3] = True
            dist[next3] = min(dist[next3], dist[now])
            queue.append(next3)
            
        if not visited[next2] and 0 <= next2 <= 100000:
            visited[next2] = True
            dist[next2] = min(dist[next2], dist[now] + 1)
            queue.append(next2)
            
        if not visited[next1] and 0 <= next1 <= 100000:
            visited[next1] = True
            dist[next1] = min(dist[next1], dist[now] + 1)
            queue.append(next1)
    


bfs(a, b)
print(dist[b])
