class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # one liner
        return str(x) == str(x)[::-1]
        
        s = str(x)
        l = len(s)
        # split the string x into 2 parts and determine each part's length
        sub = int(l/2)
        mod = l & 1  # set modulo if there's one exact middle char in x
        left = s[:sub]
        right = s[sub+mod:][::-1]
        print(left + "+" + right)
        return left == right
