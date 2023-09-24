// Given a string s, reverse only all the vowels in the string and return it.

// The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution {
public:
    bool isVowel(char x) {
        x = tolower(x);
        return x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u';
    }

    string reverseVowels(string s) {
        int i = 0; // Left pointer
        int j = s.size() - 1; // Right pointer

        while (i < j) {

            // Move i to next vowel
            while (i < j && !isVowel(s[i])) i++;

            // Move j to next vowel
            while (i < j && !isVowel(s[j])) j--;

            // Swap vowels and increment pointers
            swap(s[i], s[j]);
            i++;
            j--;
        }

        return s;
    }
};
