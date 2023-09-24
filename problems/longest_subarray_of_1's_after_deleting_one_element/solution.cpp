// Given a binary array nums, you should delete one element from it.

// Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int l = 0, zeros = 0, ans = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r] == 0) {
                zeros++;
            }
            if (zeros > 1 && nums[l++] == 0) {
                zeros--;
            }
            ans = max(ans, r - l);
        }
        return ans;
    }
};
