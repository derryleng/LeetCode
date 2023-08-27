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