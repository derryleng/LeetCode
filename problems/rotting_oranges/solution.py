# You are given an m x n grid where each cell can have one of three values:

#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque()
        fresh_count = 0

        # Enqueue "rotten" (2) and count "fresh" (1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2: 
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0

        # BFS
        minutes = 0
        while queue:
            i, j, minutes = queue.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                    grid[x][y] = 2
                    queue.append((x, y, minutes + 1))
                    fresh_count -= 1
        
        return minutes if fresh_count == 0 else -1
