
def reverse(x):
    
    if x>=0:
        n = str(x)
        y = [char for char in n]
        
        l =""
        r = len(y)
        
        for m in range(r):
            l = l + y[r-m-1]
        
        if int(l) > 2147483647:
            return (0)
        else:
            return (int(l))
        

    else:
        xx= -1*x
        n = str(xx)
        y = [char for char in n]
        
        l =""
        r = len(y)
        
        for m in range(r):
            l = l + y[r-m-1]
        
        if int(l) > 2147483648:
            return (0)
        else:
            return (-1*int(l))
        

print(reverse(-123456))