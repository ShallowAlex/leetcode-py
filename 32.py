class Solution:
    def longestValidParentheses(self, s: str) -> int:
        biggest = 0
        left = 0
        right = 0
        for i in s:
            if i == "(":
                left += 1
            else:
                right += 1
                if left < right:
                    left = right = 0
            if left == right:
                biggest = max(biggest, left*2)
        left = right = 0
        for i in s[::-1]:
            if i == ")":
                right += 1
            else:
                left += 1
                if right < left:
                    left = right = 0
            if left == right:
                biggest = max(biggest, left*2)
        return biggest