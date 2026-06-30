class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges)!= n-1:
            return False
        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        stack = [0]
        seen = set([0])
        while stack:
            node = stack.pop()
            for v in adj[node]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return len(seen)==n