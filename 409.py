class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        dic = Counter(s)
        count = 0
        for w in dic:
            count += dic[w] // 2 * 2
        if count < len(s):
            count += 1
        return count