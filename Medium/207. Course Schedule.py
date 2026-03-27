class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Build graph
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        path = set()   # current DFS recursion stack
        safe = set()   # nodes already confirmed safe

        def dfs(node):
            # cycle detected
            if node in path:
                return False

            # already processed
            if node in safe:
                return True

            path.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            path.remove(node)
            safe.add(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
