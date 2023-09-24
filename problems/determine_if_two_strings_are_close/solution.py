# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

class Solution:
    def countOccurences(self, string: str) -> dict:
        occurences = {}
        for i in string:
            if i in occurences:
                occurences[i] += 1
            else:
                occurences[i] = 1
        return occurences

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        # if sorted(set([*word1])) == sorted(set([*word2])):
        #     return True
        occ1 = self.countOccurences(word1)
        occ2 = self.countOccurences(word2)
        if sorted(occ1.values()) == sorted(occ2.values()) and sorted(occ1.keys()) == sorted(occ2.keys()):
            return True
        return False