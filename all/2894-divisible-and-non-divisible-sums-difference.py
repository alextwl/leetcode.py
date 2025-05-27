'''
2025/05/27 daily challenge

math approach
'''


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return (n * (n+1) // 2) - sum(range(m, n+1, m)) * 2


'''
sum of arithmetic sequence approach

      n
Sn = ---(a + an)
      2

      n
   = ---(2*a + (n - 1) * d)
      2

               n * (n - 1)
   = a*n + d * -----------
                    2
'''


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        l = n // m
        return (n * (n+1) // 2) - (m * l + m * (l * (l-1)) // 2) * 2

