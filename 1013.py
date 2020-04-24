class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        s = s // 3
        total = 0
        index1 = index2 = -1
        for i in range(len(A)-1):
            total += A[i]
            if index1 == -1 and total == s:
                index1 = i
                continue
            if index1 != -1 and total == 2*s:
                index2 = i
                break
        return True if index1 < index2 else False