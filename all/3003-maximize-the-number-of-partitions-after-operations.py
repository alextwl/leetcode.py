'''
2025/10/17 daily challenge

bitwise + two-way enumeration approach

learnt from official editorial:
https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/editorial/#approach-bitwise-operations--preprocessing--enumeration
'''


ASCII_A = ord('a')


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        left = [[0, 0, 0]]
        right = [[0, 0, 0]]

        val, mask, cnt = 0, 0, 0
        for c in s[:-1]:
            bits = 1 << (ord(c) - ASCII_A)
            if not (bits & mask):
                cnt += 1
                if cnt <= k:
                    mask |= bits
                else:
                    val += 1
                    mask = bits
                    cnt = 1
            left.append([val, mask, cnt])

        val, mask, cnt = 0, 0, 0
        for c in s[-1:0:-1]:
            bits = 1 << (ord(c) - ASCII_A)
            if not (bits & mask):
                cnt += 1
                if cnt <= k:
                    mask |= bits
                else:
                    val += 1
                    mask = bits
                    cnt = 1
            right.append([val, mask, cnt])
        right.reverse()

        max_val = 0
        for ltuple, rtuple in zip(left, right):
            # base case: left & right contributes 2 segments
            seg_count = ltuple[0] + rtuple[0] + 2
            bit_count = (ltuple[1] | rtuple[1]).bit_count()
            if ltuple[2] == k and rtuple[2] == k and bit_count < 26:
                # have chance to replace a character for one more segment
                seg_count += 1
            elif min(bit_count + 1, 26) <= k:
                # even if we've replaced a char,
                # merging left + right contributes only one segment
                seg_count -= 1
            max_val = max(max_val, seg_count)
        return max_val

