from collections import deque

visited = [False] * n

for i in range(n):
    if not visited[i]:
        q = deque([i])
        visited[i] = True

        while q:
            u = q.popleft()
            print(u, end=" ")

            for neighbor in adj[u]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
