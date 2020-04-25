class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        res = re.sub(r'[^0-9a-zA-Z]', '', s)
        res = res.upper()
        left = 0
        right = len(res) - 1
        while left < right:
            if res[left] == res[right]:
                left += 1
                right -= 1
            else:
                return False
        return True