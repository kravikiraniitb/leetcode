class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        f_ar = []
        b_ar = []
        for x in range(n):
            f_ar.append("(")

        for x in range(n):
            b_ar.append(")")

        #t = 2**(2*n)
        arr = []
        #()()()
    def factorial(f):
        if (f == 0 or f ==1):
            return 1

        return f*factorial(f-1)

        c= int(factorial(2*n)/(factorial(n)*factorial(n)))

        for y in range(c):
            n=0
            m=0

