class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        lengh = 0
        x1 = x
        while x1:
            lengh += 1
            x1 = x1//10
        half = lengh//2
        for i in range(half):
            if (x//10**i)%10 != x//(10**(lengh-i-1))%10:
                return False
        return True


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x//10 != 0):
            return False
        tmp = 0
        while tmp < x:
            tmp = tmp*10 + x%10
            x = x//10
        return x == tmp or x == tmp//10