def letterCombinations(digits):

    a_d = [char for char in digits]

    l = len(digits)
    fa =[]
    dt = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y", "z"]
    }

    if l == 0:
        return []
    elif l == 1:
        return dt[a_d[0]]
    elif l == 2:
        w =""
        for x in dt[a_d[0]]:
            for y in dt[a_d[1]]:
                w=x+y
                fa.append(w)
        return fa

    elif l == 3:
        w =""
        for x in dt[a_d[0]]:
            for y in dt[a_d[1]]:
                for z in dt[a_d[2]]:
                    w=x+y+z
                    fa.append(w)
        return fa
    else:
        w =""
        for x in dt[a_d[0]]:
            for y in dt[a_d[1]]:
                for z in dt[a_d[2]]:
                    for k in dt[a_d[3]]:
                        w=x+y+z+k
                        fa.append(w)
        return fa
    
print(letterCombinations("23"))


