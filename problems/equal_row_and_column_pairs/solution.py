# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = [" ".join(str(j) for j in i) for i in grid]
        cols = [" ".join(str(grid[i][j]) for i in range(len(grid))) for j in range(len(grid))]
        pairs = 0
        for r in rows:
            for c in cols:
                if r == c:
                    pairs += 1
        return pairs