from collections import deque

def bfs(start, adj):
    n = len(adj)
    visited = [False] * n
    q = deque()

    visited[start] = True
    q.append(start)

    while q:
        u = q.popleft()
        print(u, end=" ")

        for neighbor in adj[u]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)


bfs(0, adj)
