class Solution {
public:
    bool canPlaceFlowers(vector<int>& v, int n) {
        int vSize = v.size();
        
        for (int i = 0; i < vSize; i++) {
            if (
                v[i] == 0 &&
                (i == 0 || v[i - 1] == 0) &&
                (i == vSize - 1 || v[i + 1] == 0)
            ) {
                v[i] = 1;
                n--;
            }
        }

        return n <= 0;
    }
};