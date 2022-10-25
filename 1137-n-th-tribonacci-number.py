class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in [1,2]:
            return 1
        
        # dp space
        t = [0] * (n+1)
        # base case
        t[1], t[2] = 1, 1
        
        for i in range(3, n+1):
            '''
            rewrite the equation to:
            Tn = Tn-3 + Tn-2 + Tn-1
            '''
            t[i] = t[i-3] + t[i-2] + t[i-1]
        
        return t[n]
