from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
         k- source node
         need to find the max d(k,v) : v in G

         single source shortest path problem - djikstra works for nonngeative weights


         1 -> 0 
         |
         v
         2 -> 3
        """
        adjacency = defaultdict(list)
        for u,v,w in times:
            adjacency[u-1].append((v-1,w))
        
        dist = [float("inf")]*n
        dist[k-1] = 0

        heap = [(0,k-1)]
        heapq.heapify(heap)
        while heap:
            #print(heap)
            distance, node = heapq.heappop(heap)
            if dist[node] < distance:
                continue
            
            for neighbor,weight in adjacency[node]:
                if weight+ distance < dist[neighbor]:
                    dist[neighbor] = weight+distance
                    heapq.heappush(heap, (dist[neighbor], neighbor))

        return -1 if max(dist)== float("inf") else max(dist)