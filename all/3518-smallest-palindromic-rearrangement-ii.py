'''
2026/07/29 daily challenge

combinatorics + permutations + try and error approach

learnt from official editorial:
https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/editorial/#approach-combinatorial-mathematics--trial-and-error-method
'''


ASCII_A = ord('a')


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        half = len(s) >> 1
        buckets = [0] * 26

        for v in map(ord, s[:half]):
            buckets[v - ASCII_A] += 1

        def comb(n, m, limit):
            ret = 1
            m = min(m, n - m)
            for i in range(1, m + 1):
                ret = ret * (n - i + 1) // i
                if ret > limit:
                    return limit + 1
            return ret

        def perm(rem):
            ways = 1
            for cnt in buckets:
                if not cnt:
                    continue
                ways = ways * comb(rem, cnt, k)
                if ways > k:
                    break
                rem -= cnt
            return ways

        prefix = []
        start_th = 1
        for pos in range(half):
            for i in range(26):
                if not buckets[i]:
                    continue

                buckets[i] -= 1
                ways = perm(half - pos - 1)
                if start_th + ways > k:
                    # at least k-th lexicographical smallest, fix the char
                    prefix.append(chr(ASCII_A + i))
                    break
                buckets[i] += 1
                start_th += ways
        
        if len(prefix) < half:
            return ""

        center = s[half] if len(s) & 1 else ""
        return ''.join(prefix) + center + ''.join(reversed(prefix))

