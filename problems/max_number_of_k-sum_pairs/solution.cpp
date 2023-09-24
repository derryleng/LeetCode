// You are given an integer array nums and an integer k.

// In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

// Return the maximum number of operations you can perform on the array.

class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int i = 0, j = nums.size() - 1, count = 0;
        while (j > i) {
            if (nums[i] + nums[j] == k) {
                count++;
                i++;
                j--;
            }
            else if (nums[i] + nums[j] < k) {
                i++;
            }
            else {
                j--;
            }
        }
        return count;
    }
};
