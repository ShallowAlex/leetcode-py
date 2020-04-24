class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        pre = self.countAndSay(n - 1)
        tmp = []
        count = 0
        number = 0
        for i in range(len(pre)):
            if pre[i] != number:
                tmp.append(str(count))
                tmp.append(str(number))
                number = pre[i]
                count = 1
            else:
                count += 1
        tmp.pop(0)
        tmp.pop(0)
        tmp.append(str(count))
        tmp.append(str(number))
        return ''.join(tmp)