'''
2023/02/01 daily challenge

calculate the possibly largest GCD string and decrease its length while trying.
'''

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isDivisible(target, gcd_str):
            '''
            verify if target string is divisible by gcd_str.
            '''
            gcd_len = len(gcd_str)
            for i in range(gcd_len, len(target)+1, gcd_len):
                if target[i-gcd_len:i] != gcd_str:
                    return False
            return True
        
        n1, n2 = len(str1), len(str2)
        max_gcd_len = math.gcd(n1, n2)
        # start trying from the largest possible GCD string.
        for g in range(max_gcd_len, 0, -1):
            x = str1[:g]
            if isDivisible(str1, x) and isDivisible(str2, x):
                return x

        return ""

