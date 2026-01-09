
# number of vertices
n = 5

# adjacency list
adj = [
    [1, 2],   # 0
    [3],      # 1
    [4],      # 2
    [],       # 3
    []        # 4
]



def dfs(u,adj,visited):
  visited[u]=True
  print(u, end=" ")

  for neighbour in adj[u]:
    if not visited[neighbour]:
      dfs(neighbour,adj,visited)



visited = [False] * n
dfs(0, adj, visited)
