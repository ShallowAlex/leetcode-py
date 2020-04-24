class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = 0
        s = s[::-1]
        for i in s:
            if i == ' ':
                last += 1
            else:
                break
        s = s[last:]
        last = 0
        for i in s:
            if i == ' ':
                break
            last += 1
        return last

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        bs = 0
        lengh = len(s)
        for i in range(lengh-1, -1, -1):
            if s[i] != ' ':
                break
            bs += 1
        for i in range(lengh-1-bs, -1, -1):
            if s[i] == ' ':
                break
            count += 1
        return count

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1]) if s else 0