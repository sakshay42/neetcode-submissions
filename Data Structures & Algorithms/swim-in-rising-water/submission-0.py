class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dist = [[float("inf")] * n for _ in range(n)]
        dist[0][0] = grid[0][0]

        heap = [(grid[0][0], 0, 0)]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            t, x, y = heapq.heappop(heap)

            if (x, y) == (n - 1, n - 1):
                return t

            if t > dist[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    nt = max(t, grid[nx][ny])

                    if nt < dist[nx][ny]:
                        dist[nx][ny] = nt
                        heapq.heappush(heap, (nt, nx, ny))