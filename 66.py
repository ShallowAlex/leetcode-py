class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1

        while digits[index] == 9:
            digits[index] = 0
            index -= 1
            if index == -1:
                digits.insert(0, 1)
                return digits
        digits[index] += 1
        return digits