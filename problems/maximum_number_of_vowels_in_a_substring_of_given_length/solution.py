class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = sum(1 for x in s[:k] if x in vowels)
        max_count = count
        # print(s[:k], count)
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                count -= 1
            if s[i + k - 1] in vowels:
                count += 1
            # print(s[i:(i+k)], s[i - 1], s[i+k-1], count)
            max_count = max(max_count, count)
        return max_count
