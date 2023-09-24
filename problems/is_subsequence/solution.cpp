class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sSize = s.size(), tSize = t.size();
        int sInd = 0, tInd = 0;
        while (tInd < tSize && sInd < sSize) {
            if (s[sInd] == t[tInd]) {
                sInd++;
            }
            tInd++;
        }
        return sInd == sSize;
    }
};
