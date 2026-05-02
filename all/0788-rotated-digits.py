'''
2026/05/02 daily challenge

brute force approach
'''


class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for s in map(str, range(1, n + 1)):
            # ignore 018, check if there's at least one digit
            # could be rotated to another different digit,
            # and exclude those cannot be rotated.
            if any(c in "2569" for c in s) and not any(c in "347" for c in s):
                ans += 1
        return ans


'''
dynamic programming (for prefix digits) approach

it also goes through entire [1, n] but optimized for validation.
during iteration, we only validate last digit and
retrieve type of prefix from dp space.
'''


class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        # dp[i] = type of number i
        # 0: invalid (has digits '347' unable to rotate)
        # 1: unchanged after rotated (has only '018' digits)
        # 2: changed after rotated (no invalids and has at least one digit from '2569')
        dp = [0] * (n + 1)

        # base case < 10
        for i in range(min(10, n + 1)):
            if i in {0, 1, 8}:
                # rotated unchanged
                dp[i] = 1
            elif i in {2, 5, 6, 9}:
                # rotated & changed
                dp[i] = 2
                ans += 1

        # for case >= 10
        for i in range(10, n + 1):
            quo, rem = divmod(i, 10)
            a, b = dp[quo], dp[rem]  # prefix type, suffix type
            if a == 1 and b == 1:
                # rotated unchanged
                dp[i] = 1
            elif a >= 1 and b >= 1:
                # rotated & changed
                dp[i] = 2
                ans += 1
            # if there's a type-0 between prefix & suffix, it's invalid.

        return ans

