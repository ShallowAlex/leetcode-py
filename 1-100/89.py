class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        head = 1
        for i in range(n):
            l = len(ans)
            for j in range(l)[::-1]:
                ans.append(head + ans[j])
            head *= 2
        return ans

#方法2（菜鸡方法）
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        if n == 0:
            return [0]
        for i in range(2**n):
            gray = []
            tmp1 = list(bin(i)[2:].zfill(n))
            tmp2 = list(bin(i>>1)[2:].zfill(n))
            for i in range(n):
                gray.append(str(int(tmp1[i]) ^ int(tmp2[i])))
            ans.append(int(''.join(gray),2))
        return ans
