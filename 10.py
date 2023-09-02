#Git
def isMatch(s, p):
    a_s = [char for char in s]
    p_ss = [char for char in p]
    #print("a_s")
    print(a_s)
    #print("p_ss")
    print(p_ss)

    bool = False
    
    #"ab"
    #".*"

    if "*" in p_ss:
        p_s = p_ss.copy()
        bool = True
        
        for x in range(len(a_s)):
           
            if a_s[x] == p_s[x]:
                bool = True
                
            elif p_s[x] == "*":
                
                ap = p_s[x -1]
                if a_s[x] == ap:
                    p_s.insert(x,ap)
                
                elif p_s[x -1] == ".":
                    bool = True
                else:
                    if x < len(p_s) - 1:
                    
                        if a_s[x] == p_s[x +1]:
                            p_s.pop(x)
                            
                        else:
                            bool = False
                            
                            break
                    else:
                        bool = False
                            
                        break
            
            elif p_s[x] == ".":
                bool = True
                #print("5")
            else:
                bool = False
                #print("6")
                break
        #print("3")
        #print(p_ss)

        #print("4")

        print(p_s)
        
    else:
        bool = False
        p_s = p_ss.copy()
        if len(a_s) == len(p_s):
                for a in a_s:
                    for p in p_s:
                        if a==p:
                            bool=True
                        elif p == ".":
                            bool = True
                        else:
                            bool = False
                            break
        else:
            bool = False


    return bool


print(isMatch("mississippi", "mis*is*p*."))
