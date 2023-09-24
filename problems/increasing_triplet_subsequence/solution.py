# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = inf, inf

        for k in nums:
            if j < k:
                return True

            if k <= i:
                i = k
            else:
                j = k

        return False
