'''
2025/04/22 daily challenge

combinatorial + dynamic programming approach

learnt from official editorial:
https://leetcode.com/problems/count-the-number-of-ideal-arrays/editorial/

good explanation to read:
https://leetcode.com/problems/count-the-number-of-ideal-arrays/solutions/6675762/explaining-the-editorial-by-kosievdmerwe-gvhh/
'''


MOD = 1_000_000_007
MAX_N = 10010
MAX_P = 15  # max 15 prime factors

# build sieve
sieve = [0] * MAX_N
for i in range(2, MAX_N):
    if sieve[i] == 0:
        for j in range(i, MAX_N, i):
            sieve[j] = i

ps = [list() for _ in range(MAX_N)]
for i in range(2, MAX_N):
    x = i
    psi = ps[i]
    while x > 1:
        p = sieve[x]
        count = 0
        while (qr := divmod(x, p))[1] == 0:
            x = qr[0]
            count += 1
        psi.append(count)

c = [[0] * (MAX_P + 1) for _ in range(MAX_N + MAX_P)]
c[0][0] = 1
prev = c[0]
for i in range(1, MAX_N + MAX_P):
    ci = c[i]
    ci[0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        ci[j] = (prev[j] + prev[j - 1]) % MOD
    prev = ci


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0
        for v in range(1, maxValue + 1):
            mul = 1
            for p in ps[v]:
                mul = (mul * c[n + p - 1][p]) % MOD
            ans = (ans + mul) % MOD
        return ans

