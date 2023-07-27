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