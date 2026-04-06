import heapq
from collections import defaultdict
import math

class Solution:
    def networkDelayTime(self, times, N, K):
        
        # Step 1: Build adjacency list
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        # Step 2: Initialize distances
        INF = math.inf
        dist = [INF] * (N + 1)
        dist[K] = 0
        
        # Step 3: Min heap (distance, node)
        pq = [(0, K)]
        
        while pq:
            d, node = heapq.heappop(pq)
            
            # Step 4: Skip stale entries
            if d > dist[node]:
#👉 d =

#the distance value that came from the heap
#dist[2]

#👉 This is:

#the best (shortest) distance to node 2 found so far
                continue
            
            # Step 5: Relax neighbors
            for nei, w in adj[node]:
                if dist[nei] > d + w:
                    dist[nei] = d + w
                    heapq.heappush(pq, (dist[nei], nei))
        
        # Step 6: Find answer
        ans = 0
        for i in range(1, N + 1):
            if dist[i] == INF:
                return -1
            ans = max(ans, dist[i])
        
        return ans
