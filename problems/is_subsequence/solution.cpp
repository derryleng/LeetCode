// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

// A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

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
