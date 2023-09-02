class Solution:

    def substringf(self, string1):
        length = len(string1)
        list_sub = []

        for i in range(length-1):
            for x in range(length - i):
                substring = ""
                for m in range(x+1):
                    substring = substring + string1[i+m]
                list_sub.append(substring)
        print(list_sub)
        return list_sub

    def check_palindromicf(self, string2):
        length_a = len(string2)
        status = False
        for n in range(length_a):
            if string2[n] != string2[length_a-1-n]:
                status = False
                break
            else:
                status = True
        return status
        
    def longestPalindrome(self, s: str) -> str:
        substrings = self.substringf(s)
        if len(s) == 1:
            return s
        elif len(s) == 0:
            return None
        else:
            list_pal = []
            for h in substrings:
                if self.check_palindromicf(h):
                    list_pal.append(h)
            
            if len(list_pal) > 1:
                return max(list_pal, key=len)
            elif len(list_pal) == 1:
                return list_pal[0]
            else:
                return None


# Step 1: Create an instance of the Solution class
solution = Solution()

# Step 2: Call longestPalindrome function with different input strings
input_string1 = "lajsbdlajsbcnadddddddddddddalnlnlnlnlnlnlnlnlnlnlnlkn"
result1 = solution.longestPalindrome(input_string1)
print("Longest palindrome:", result1)
