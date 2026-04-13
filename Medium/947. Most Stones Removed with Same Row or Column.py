class Solution:
    def removeStones(self, stones):
        parent = {}
        rank = {}

        def find(x):
            if x != parent.setdefault(x, x):
                parent[x] = find(parent[x])   # path compression
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return

            # union by rank
            if rank.get(px, 0) < rank.get(py, 0):
                parent[px] = py
            elif rank.get(px, 0) > rank.get(py, 0):
                parent[py] = px
            else:
                parent[py] = px
                rank[px] = rank.get(px, 0) + 1

        # connect row and column
        for r, c in stones:
            union(r, ~c)
            🔥 Why we use ~c (i.e., -c - 1)
Problem:

Rows and columns are both numbers.

Example:

row = 2
col = 2

If you do:

union(2, 2)

👉 You’re saying:

row 2 == column 2

🚨 WRONG — they are different things.

✅ Solution: Separate their identities

We need:

rows → one space
columns → another space

        # count unique components
        roots = set()
        for x in parent:
            roots.add(find(x))

        return len(stones) - len(roots)
