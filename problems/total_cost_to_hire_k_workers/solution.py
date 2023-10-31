# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

# You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

#   - You will run k sessions and hire exactly one worker in each session.
#   - In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
#       - For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
#       - In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
#   - If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
#   - A worker can only be chosen once.

# Return the total cost to hire exactly k workers.

from heapq import heapify, heappush, heappop

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l = [] # Left queue
        r = [] # Right queue
        i = 0 # Left pointer
        j = len(costs) - 1 # Right pointer
        ans = 0

        for _ in range(k):

            # Populate heaps to size
            while len(l) < candidates and i <= j:
                heappush(l, costs[i])
                i += 1
            while len(r) < candidates and i <= j:
                heappush(r, costs[j])
                j -= 1

            if (l and r and l[0] <= r[0]) or (l and not r):
                ans += l[0]
                heappop(l)
            elif (l and r and l[0] > r[0]) or (r and not l):
                ans += r[0]
                heappop(r)

        return ans
