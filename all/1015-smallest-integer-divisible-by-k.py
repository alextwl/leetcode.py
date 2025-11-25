'''
2025/11/25 daily challenge

modular arithmetic approach

similar to problem 1018,
it's not asking for prefix Xi = (Rem(i-1) * 2 + nums[i]) % 5
but for Xi = (Rem(i-1) * 10 + 1) % k.
the induction is the compatible for both problems.
'''


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rem = 1
        ans = 1
        # if not divisible, the remainder eventually starts repeating
        seen = set()
        while (rem := rem % k):
            if rem in seen:
                return -1
            seen.add(rem)
            rem = rem * 10 + 1
            ans += 1
        return ans

