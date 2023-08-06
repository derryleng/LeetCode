class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        if (n == 1) return 1;

        int newInd = 0;
        for(int i = 1, count = 1; i <= n; i++, count++) {
		    if (i == n || chars[i] != chars[i - 1]) {
                chars[newInd++] = chars[i - 1];  
                
                if (count > 1) {
                    for (char digit : to_string(count)) {
                        chars[newInd++] = digit;
                    }
                }

                count = 0;
            }
        }
        return newInd;
    }
};