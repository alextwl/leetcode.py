'''
2026/01/04 daily challenge

memorization approach
'''


SEEN = {}


def find_divisors(val):
    divisors = [1, val]

    # avoid duplicate square root divisor
    sqrt = int(val ** 0.5)
    if sqrt * sqrt == val:
        divisors.append(sqrt)

    # check [2, sqrt)
    for div in range(2, sqrt):
        quo, rem = divmod(val, div)
        if rem == 0:
            divisors.append(div)
            divisors.append(quo)
            if len(divisors) > 4:
                break

    SEEN[val] = sum(divisors) if len(divisors) == 4 else 0


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for v in nums:
            if v not in SEEN:
                find_divisors(v)
            ans += SEEN[v]
        return ans

