def factorial(f):
        if (f == 0 or f ==1):
            return 1

        return f*factorial(f-1)
n=2
print(int(factorial(2*n)/(factorial(n)*factorial(n))))