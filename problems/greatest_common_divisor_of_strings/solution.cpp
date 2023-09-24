// For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

// Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 == str2 + str1) {
            return str1.substr(0, gcd(str1.size(), str2.size()));
        }
        else {
            return "";
        }
    }
};
