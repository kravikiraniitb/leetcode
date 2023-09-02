
def palindrome(string):

    y = [*string]
    l = len(y)
    #result = False

    for i in range(l):
        if y[i] == y[l-i-1]:
            result = True
        else:
            result = False
            break

    return result
print(palindrome("12121"))
