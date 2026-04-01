from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        # 1. Build the Directed Graph using an adjacency list
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            u, v = equations[i]
            val = values[i]
            # Add edge u -> v with weight val
            graph[u].append((v, val))
            # Add edge v -> u with weight 1/val
            graph[v].append((u, 1.0 / val))

        # 2. DFS Function to find the path and multiply weights
        def dfs(curr, target, running_product, visited):
            # If we reached the target node, return the accumulated product
            if curr == target:
                return running_product
            
            visited.add(curr)
            
            # Inner loop: explore neighbors
            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    # Recursive call with updated product
                    res = dfs(neighbor, target, running_product * weight, visited)
                    # If the result is valid, pass it back up the stack
                    if res != -1.0:
                        return res
            
            return -1.0

        final_results = []

        # 3. Outer loop for the inputs (u and v)
        for u, v in queries:
            if u not in graph or v not in graph:
                # If node doesn't exist, result is -1.0
                final_results.append(-1.0)
            elif u == v:
                # If u and v are the same node, result is 1.0
                final_results.append(1.0)
            else:
                # Perform search with a fresh visited set for each query
                visited = set()
                result = dfs(u, v, 1.0, visited)
                final_results.append(result)

        return final_results
