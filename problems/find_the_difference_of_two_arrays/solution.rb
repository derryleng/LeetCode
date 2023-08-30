# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[][]}
def find_difference(nums1, nums2)
    n1 = nums1.uniq
    n2 = nums2.uniq
    return [n1 - n2, n2 - n1]
end