def isMatch(s, p):
    a_s = [char for char in s]
    p_s = [char for char in p]

    bool = False
    
    #"aab"
    #"c*a*b"

    if "*" in p_s:
        bool = True
        p_s_r = p_s[::-1]
        li = len(p_s) - 1 - p_s_r.index("*")

        left = len(p_s) - li -1

        for x in range(left):
            if a_s[-1-x] == p_s[-1-x]:
                bool = True
            elif p_s[-1-x] == ".":
                bool = True
            else:
                bool = False
                break


        
    else:
        bool = False
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