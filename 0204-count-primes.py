class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        # http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        isPrime = [True] * (n)
        isPrime[0] = isPrime[1] = False
        
        i = 2
        while(i*i < n):
            if not isPrime[i]:
                i += 1
                continue
            j = i*i
            while(j < n):
                isPrime[j] = False
                j += i
            i += 1
        
        count = 0
        for i in range(2,n):
            if isPrime[i]:
                count += 1
        
        return count
