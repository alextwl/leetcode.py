'''
2024/03/13 daily challenge

prefix sum approach
'''


class Solution:
    def pivotInteger(self, n: int) -> int:
        suffix = (n * (n + 1)) // 2
        
        prefix = 0
        for x in range(n + 1):
            prefix += x
            if prefix == suffix:
                return x
            suffix -= x

        return -1


'''
math approach

learnt from official solution
https://leetcode.com/problems/find-the-pivot-integer/solution/

intuition:

(1) 1 + 2 + ... + x == x + (x+1) + ... + n

    x * (x+1)    (x+n)*(n-x+1)
(2) --------- == -------------
        2              2

    x**2 + x    xn - x**2 + x + n**2 - nx + n
(3) -------- == -----------------------------
        2                    2

            (n**2 + n)
(4) x**2 == ----------
                 2

          n**2 + n
(5) x == (--------) ** 0.5
              2
'''


class Solution:
    def pivotInteger(self, n: int) -> int:
        sigma = (n * (n + 1)) // 2
        pivot = int(sigma ** 0.5)
        
        return pivot if pivot * pivot == sigma else -1

