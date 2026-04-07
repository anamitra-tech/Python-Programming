class Solution:
    def dfs(self, node, c, graph, color):
        color[node] = c

        for nei in graph[node]:
            if color[nei] == 0:
                if not self.dfs(nei, -c, graph, color):
                    return False
            elif color[nei] == color[node]:
                return False  # same color on both sides

        return True

    def isBipartite(self, graph):
        n = len(graph)
        color = [0] * n  # 0 = unvisited, 1 and -1 = colors

        for i in range(n):
            if color[i] == 0:
                if not self.dfs(i, 1, graph, color):
                    return False

        return True
