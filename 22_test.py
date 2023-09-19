ar2=[]
ar3=[]
def generateParenthesis(n):
    def one_l():
        ar2_c = ar2.copy()
        ar2.append("(")
        ar3.append(ar2)
        ar2_c.append(")")
        ar3.append(ar2_c)

    while len(ar3) <= 2**n:
        one_l()
    return ar3

print(generateParenthesis(2))