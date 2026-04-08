class Solution:
    def allPathsSourceTarget(self, graph):
        res = []
        target = len(graph) - 1
        path = [0]

        def dfs(node):
            if node == target:
                res.append(path[:])
                return

            for nei in graph[node]:
                path.append(nei)
                dfs(nei)
                path.pop()

        dfs(0)
        return res
