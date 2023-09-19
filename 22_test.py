ar2=[]
ar3=[[]]
def generateParenthesis(n):
    def one_l():
        #ar2_c = ar2.copy()
        for x in ar3:
            x1 = x.copy()
            x2 = x.copy()

            x1.append("(")
            x2.append(")")
            ar3.remove(x)
            ar3.append(x1)
            ar3.append(x2)
            #print(ar3)
            break
            print(ar3)

    while len(ar3) < 2**n:
        one_l()
    #return ar3
    ar4=[]
    for y in ar3:
        m=0
        n=0
        for z in y:
            if z == "(":
                m=m+1
            else:
                n=n+1
                if n>m:
                    break

print(generateParenthesis(2))