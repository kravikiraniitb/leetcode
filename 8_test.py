class Solution:
    def myAtoi(self, s: str) -> int:
        y = [char for char in s]
        l =""
        n=0
        a =""
        for x in y:
            if x == " ":
                n=n+1
            else:
                break

        y2 = []
        for x in range(n,len(y)):
            y2.append(y[x])
        a =""
        if y2[0] == "-":
            a = "-"
            del y2[0]
        
        for x2 in y2:
            if x2.isdigit():
                l = l+x2
            else:
                break
        

        l2 = a+l
        if ((l2 =="") or (l2 =="+") or (l2 =="-")):
            return(0)
        else:
            if int(l2) > 2147483647:
                return(2147483647)
            
            
            elif int(l2) < -2147483648:
                return(-2147483648)
            
            else:
                return(int(l2))
