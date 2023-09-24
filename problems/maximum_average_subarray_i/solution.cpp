// You are given an integer array nums consisting of n elements, and an integer k.

// Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        int currentSum = 0;
        for (int i = 0; i < k; i++) {
            currentSum += nums[i];
        }
        int maxSum = currentSum;
        if (k < n) {
            int l = 0, r = k - 1;
            while (r < n) {
                int newSum = currentSum - nums[l++] + nums[++r];
                if (newSum > maxSum) {
                    maxSum = newSum;
                }
                currentSum = newSum;
            }
        }
        return (double)maxSum / k;
    }
};
