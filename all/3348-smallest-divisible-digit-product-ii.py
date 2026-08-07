'''
2026/08/07 daily challenge

enumeration + greedy method approach

learnt from official editorial:
https://leetcode.com/problems/smallest-divisible-digit-product-ii/editorial/#approach-enumerate-the-string-from-right-to-left
'''


import math


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        n = len(num)
        tt = t
        for i in range(2, 10):
            while tt % i == 0:
                tt = tt // i
        if tt > 1:
            return "-1"

        rem = [0] * (n + 1)
        rem[0] = t
        pos = n - 1

        dig = list(map(int, num))
        for i in range(n):
            if dig[i] == 0:
                pos = i
                break
            rem[i + 1] = rem[i] // math.gcd(rem[i], dig[i])

        if rem[-1] == 1:
            # product of num is divisible by t.
            return num

        # suffix
        for i in range(pos, -1, -1):
            while True:
                dig[i] += 1
                if dig[i] > 9:
                    break

                tt = rem[i] // math.gcd(rem[i], dig[i])
                k = 9
                for j in range(n - 1, i, -1):
                    while tt % k != 0:
                        k -= 1
                    tt = tt // k
                    dig[j] = k
                if tt == 1:
                    return ''.join(map(str, dig))

        ans = []
        orig_t = t
        for i in range(9, 1, -1):
            while orig_t % i == 0:
                ans.append(str(i))
                orig_t = orig_t // i

        s_ans = "".join(reversed(ans))
        pad = max(n + 1 - len(s_ans), 0)
        s_ans = "1" * pad + s_ans
        return s_ans

