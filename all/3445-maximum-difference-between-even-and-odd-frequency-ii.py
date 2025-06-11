'''
2025/06/11 daily challenge

prefix sums (parity status) + bitmasking + two pointers approach

learnt from solution by @ncann123
https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/solutions/6831146/easy-to-understand-explanation-for-editorial-solution
'''


CHARS = ['0', '1', '2', '3', '4']


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def get_parity_status(count_a, count_b):
            # bit 1: a's parity
            # bit 0: b's parity
            return ((count_a & 1) << 1) | (count_b & 1)
        
        n = len(s)
        ans = float('-inf')
        # fix two characters: iterate all possible combinations
        for a in CHARS:
            for b in CHARS:
                if a == b: continue

                # min delta (prev_a - prev_b) of parity states 00, 01, 10, 11
                best = [float('inf')] * 4

                # prefix counts for right pointer (s[0...right])
                curr_a = curr_b = 0
                # prefix counts for left pointer (s[0...left])
                prev_a = prev_b = 0
                left = -1

                for right in range(0, n):
                    if s[right] == a:
                        curr_a += 1
                    elif s[right] == b:
                        curr_b += 1

                    while (right - left >= k and curr_b - prev_b >= 2):
                        left_status = get_parity_status(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                        left += 1
                        if s[left] == a:
                            prev_a += 1
                        elif s[left] == b:
                            prev_b += 1

                    right_status = get_parity_status(curr_a, curr_b)
                    # determine the mask ending at i-1 (the end of previous prefix)
                    required = right_status ^ 0b10

                    if best[required] < float('inf'):
                        ans = max(ans, curr_a - curr_b - best[required])

        return ans

