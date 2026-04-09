❌ Why NOT work on original graph?

Suppose you try working directly:

2 → 5

You mark 5 safe.
Now question:

👉 How do you “inform” node 2 that 5 is safe?

You can’t efficiently go backward in the original graph.

Because:

Graph stores: 2 → 5
But you need: who points to 5?
💡 That’s WHY reverse graph

We create:

5 → 2

Now when 5 becomes safe:
👉 You can immediately update 2



🧠 Final Mental Model (lock this in)

Each node keeps track of:

“How many unsafe paths do I still have?”

When that becomes 0 → node is safe


from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        rev = [[] for _ in range(n)]
        outdegree = [0] * n

        for i in range(n):
            for j in graph[i]:
                rev[j].append(i)
            outdegree[i] = len(graph[i])

        q = deque()
        for i in range(n):
            if outdegree[i] == 0:
                q.append(i)

        safe = [False] * n

        while q:
            node = q.popleft()
            safe[node] = True
            for prev in rev[node]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    q.append(prev)

        return [i for i in range(n) if safe[i]] 
