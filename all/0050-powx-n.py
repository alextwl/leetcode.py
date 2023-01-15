'''
calculate the power of input x manually + cut the job in half
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)

        '''
        speed up:
        x**(2n) = (x**n) * (x**n)
        x**(2n+1) = (x**n) * (x**n) * n
        and we only need to calculate x**n once.
        '''
        ans = self.myPow(x, n >> 1)
        if n & 1 == 0:
            # for x**(2n) case
            return ans * ans  # ans**2 will raise OverflowError in some cases

        # for x**(2n+1) case
        return ans * ans * x

