'''
prefix sum + combinatorics approach
'''


class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        arr = list(map(int, s))

        # prefix[i][x][y] = the number of prefix "xy" in s[:i+1]
        prefix = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        cnt = [0] * 10
        it = enumerate(arr)
        next(it)
        cnt[arr[0]] = 1
        prev = prefix[0]
        for i, c in it:
            curr = prefix[i]
            for j in range(10):
                for k in range(10):
                    # count prefix subseq with c as last (rightmost) digit
                    curr[j][k] = prev[j][k] + (cnt[j] if k == c else 0)
            cnt[c] += 1
            prev = curr
        
        # suffix[i][x][y] = the number of suffix "yx" in s[i:]
        suffix = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        cnt = [0] * 10
        cnt[arr[-1]] = 1
        prev = suffix[-1]
        for i in range(n - 2, -1, -1):
            c = arr[i]
            curr = suffix[i]
            for j in range(10):
                for k in range(10):
                    # count suffix subseq with c as last (leftmost) digit
                    curr[j][k] = prev[j][k] + (cnt[j] if k == c else 0)
            cnt[c] += 1
            prev = curr

        # the actual value of center (3rd) digit is irrelevant,
        # sum the combinations of prefixes & suffixes.
        ans = 0
        for i in range(2, n - 2):
            left, right = prefix[i - 1], suffix[i + 1]
            for j in range(10):
                for k in range(10):
                    ans = (ans + left[j][k] * right[j][k]) % 1_000_000_007

        return ans

