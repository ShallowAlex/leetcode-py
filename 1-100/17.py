class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        def letter(pw, next_digits):
            if not next_digits:
                tmp.append(pw)
            else:
                number = dic[next_digits[0]]
                for word in number:
                    letter(pw + word, next_digits[1:])

        pw = ''
        tmp = []
        if not digits:
            return tmp
        letter(pw, digits)
        return tmp