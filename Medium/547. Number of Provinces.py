class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)

        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)

        visited = set()

        def dfs(u):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count
