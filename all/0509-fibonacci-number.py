class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            # corner case
            return 0
        
        # dp space
        f = [0] * (n+1)
        # base case (btw f[0] is already initialized.)
        f[1] = 1
        
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        
        return f[n]
