class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        f_ar = []
        b_ar = []
        for x in range(n):
            f_ar.append("(")

        for x in range(n):
            b_ar.append(")")