class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        tmp = ''
        ans = []
        def backtrack(tmp, string, n):
            l = len(string)
            if l < n or l > n*3:
                #print('*')
                return
            if n == 1:
                if int(string) <= 255:
                    #print("******")
                    if l != 1 and string[0] == '0':
                        return
                    ans.append(tmp + string)
                    return
                else:
                    #print("**",string)
                    return
            else:
                index = min(3, l-n+1)
                for i in range(index):
                    #print('i=',i,'n=',n)
                    if int(string[:i+1]) <= 255:
                        if i != 0 and string[0] == '0':
                            continue
                        #print(string[:i+1], string[i+1:])
                        tmp = tmp + string[:i+1] + '.'
                        backtrack(tmp, string[i+1:], n-1)
                        #print(tmp)
                        tmp = tmp[:-i-2]
        backtrack('', s, 4)
        return ans