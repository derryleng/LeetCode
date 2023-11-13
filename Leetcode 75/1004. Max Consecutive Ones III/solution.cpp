// Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0, r = 0;
        for (r = 0; r < nums.size(); r++) {
            if (nums[r] == 0) {
                k--;
            }
            if (k < 0) {
                if (nums[l] == 0) {
                    k++;
                }
                l++;
            }
        }
        return r - l;
    }
};
