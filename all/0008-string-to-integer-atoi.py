MAX_INT32 = 2**31 - 1 
MIN_INT32 = -2**31

class Solution:
    def myAtoi(self, s: str) -> int:
        pos = 0
        maxlen = len(s)
        negative = False

        if not s: return 0
        
        # Step 1: skip leading-whitespaces
        for c in s:
            if not c.isspace():
                break
            pos += 1
        
        if pos >= maxlen: return 0

        # Step 2: sign check        
        if s[pos] == '-':
            negative = True
            pos += 1
        elif s[pos] == '+':
            pos += 1
        
        # Step 3: read digits
        ans = 0
        while(pos < maxlen):
            if not s[pos].isdigit():
                break
            ans = ans * 10 + ord(s[pos]) - ord('0')
            pos += 1
        
        if negative:
            ans = -ans
        
        if ans > MAX_INT32:
            return MAX_INT32
        if ans < MIN_INT32:
            return MIN_INT32

        return ans
