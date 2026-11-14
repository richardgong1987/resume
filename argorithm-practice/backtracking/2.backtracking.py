class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        Output = []
        n = len(digits)

        def B(i, p):
            # 1. Base case: {p}, i = n
            if i == n:
                return Output.append(p)
            # 2.  For every c in L_i,     B(i + 1, p + c)
            for c in letters[digits[i]]:
                B(i + 1, p + c)

        B(0, '')

        return Output
