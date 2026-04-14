🧩 Drill this template (burn it in your brain)

Whenever you see constraints like:

equal / connected → union
not equal / separate → check find
class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

        for i in range(ord('a'), ord('z') + 1):
            ch = chr(i)
            self.parent[ch] = ch
            self.rank[ch] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return

        # union by rank
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb

        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa

        else:
            self.parent[pb] = pa
            self.rank[pa] += 1


class Solution:
    def equationsPossible(self, equations):
        dsu = DSU()

        # Step 1: process all "=="
        for eq in equations:
            if eq[1] == '=':
                dsu.union(eq[0], eq[3])

        # Step 2: check all "!="
        for eq in equations:
            if eq[1] == '!':
                if dsu.find(eq[0]) == dsu.find(eq[3]):
                    return False

        return True
