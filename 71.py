class Solution:
    def simplifyPath(self, path: str) -> str:
        tmp = path.split('/')
        tmp = filter(None, tmp)
        ans = []
        for i in tmp:
            if i == '..':
                if ans:
                    ans.pop()
            elif i == '.':
                continue
            else:
                ans.append(i)
        return '/' + '/'.join(ans)