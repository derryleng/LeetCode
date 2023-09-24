class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for i in arr:
            if i in occ:
                occ[i] += 1
            else:
                occ[i] = 1
        if sorted(occ.values()) == sorted(set(occ.values())):
            return True
        return False
