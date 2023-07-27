class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int greatest = *max_element(candies.begin(), candies.end());
        int n = (int)candies.size();
        vector<bool> results(n);
        for (int i = 0; i < n; i++) {
            results[i] = candies[i] + extraCandies >= greatest;
        }
        return results;
    }
};