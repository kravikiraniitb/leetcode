class Solution:
    #def __init__(self, dividend, divisor):
      #  self.dividend = dividend
       # self.divisor = divisor

    def divide(self, dividend: int, divisor: int) -> int:
            
            if dividend > 2147483647:
                return 2147483647
            elif dividend < -2147483648:
                return -2147483648
            else:
                x = dividend
                m=0
                if ((dividend < 0) and (divisor < 0)):
                    while x <= divisor:
                        x = x - divisor
                        m=m+1
                    return m

                elif (dividend < 0):
                    while x <= 0-divisor:
                        x = x + divisor
                        m=m-1
                    return m
                
                elif (divisor < 0):
                    while x >= 0-divisor:
                        x = x + divisor
                        m=m-1
                    return m
                
                else:
                    while x >= divisor:
                        x = x - divisor
                        m=m+1
                    return m

divideS = Solution()
print(divideS.divide(-1,1))