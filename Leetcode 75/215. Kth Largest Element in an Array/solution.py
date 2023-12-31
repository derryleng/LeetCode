# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

from heapq import heapify, nlargest
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        return nlargest(k, nums)[-1]
