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