class Solution:
    def intToRoman(self, num: int) -> str:

        def single(num):
            if num == 9:
                return "IX"
            else:
                if num >= 5:
                    r = num%5
                    str1 = ""
                    for x in range(r):
                        str1 = str1+"I"
                    return "V"+str1
                    
                else:
                    if num == 4:
                        return "IV"
                    else:
                        str2 = ""
                        for x in range(num):
                            str2 = str2+"I"
                        return str2


        def double(num2):
            if num2 >= 90:
                r2 = num2%90
                return "XC"+single(r2)
            else:
                if num2 >= 50:
                    r3 = num2%50
                    if r3 >= 10:
                        r4 = r3%10
                        q4 = r3//10
                        str3=""
                        for y in range(q4):
                            str3 = str3+"X"
                        #return "V"+str3
                        return "L"+str3+single(r4)

                    else:
                        return "L"+single(r3)

                        
                else:
                    if num2 >= 40:
                        r5 = num2%40
                        return "XL"+single(r5)
                    else:
                        if num2 >= 10:
                            r6 = num2%10
                            q6 = num2//10
                            str4=""
                            for y in range(q6):
                                str4 = str4+"X"
                            return str4 + single(r6)
                        else:
                            return single(num2)


        def triple(num3):
            if num3 >= 900:
                r7 = num3%900
                return "CM" + double(r7)
            else:
                if num3 >= 500:
                    r8 = num3%500
                    if r8>= 100:
                        r9 = r8%100
                        q9 = r8//100
                        str5=""
                        for y in range(q9):
                            str5 = str5+"C"
                        return "D"+str5+double(r9)
                    else:
                        return "D"+ double(r8)
                else:
                    if num3>= 400:
                        r12 = num3%400
                        return "CD"+ double(r12)
                    else:
                        if num3 >= 100:
                            r10 = num3%100
                            q10 = num3//100
                            str6=""
                            for y in range(q10):
                                str6 = str6+"C"
                            return str6+double(r10)
                        else:
                            return double(num3)


        def quadruple(num4):
            if num4 >= 1000:
                r11 = num4%1000
                q11 = num4//1000
                str7=""
                for y in range(q11):
                    str7 = str7+"M"
                return str7+triple(r11)
            else:
                return triple(num4)

        return quadruple(num)      