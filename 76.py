class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        Dict = Counter(t)
        num = len(Dict)
        head = 0
        tail = 0
        n = 0
        ans = s
        for index, word in enumerate(s):
            if word not in Dict:
                continue
            Dict[word] -= 1
            if Dict[word] == 0:
                n += 1
            while (s[head] not in Dict) or (Dict[s[head]] < 0):
                if s[head] in Dict:
                    Dict[s[head]] += 1
                head += 1
            if n == num:
                if len(ans) > index - head + 1:
                    ans = s[head:index+1]
        return ans if n == num else ''