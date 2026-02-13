'''
2026/02/13 daily challenge

prefix sum approach

divide into 3 cases:
* case1: find longest subarray of single distinct char.
* case2: find longest subarray of two distinct chars of
         (a, b), (b, c), (a, c).
         use prefix sum to record index of last seen diff between
         counts of two distinct chars.
* case3: find longest subarray of three distinct chars.
         use prefix sum to record index of last seen two diffs
         (cnt[a] - cnt[b], cnt[b] - cnt[c]).
'''


import collections


ASCII_A = ord('a')


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        def case1():
            ret = 0

            i = 0
            while i < n:
                j = i
                si = s[i]
                while j < n and s[j] == si:
                    j += 1
                ret = max(ret, j - i)
                i = j
            
            return ret

        def case2(skip_char):
            c0 = 'b' if skip_char == 'a' else 'a'
            ret = 0

            i = 0
            while i < n:
                while i < n and s[i] == skip_char:
                    i += 1
                # (cnt[c0] - cnt[c1]): last seen index
                last_seen = {0: i - 1}
                diff = 0
                while i < n and s[i] != skip_char:
                    if s[i] == c0:
                        diff += 1
                    else:
                        diff -= 1
                    if diff in last_seen:
                        ret = max(ret, i - last_seen[diff])
                    else:
                        last_seen[diff] = i
                    i += 1
            return ret

        def case3():
            ret = 0
            last_seen = {(0, 0): -1}  # (diff_ab, diff_bc): last seen index
            cnt = [0, 0, 0]

            for i, c in enumerate(s):
                cnt[ord(c) - ASCII_A] += 1
                diff_ab, diff_bc = cnt[0] - cnt[1], cnt[1] - cnt[2]
                key = (diff_ab, diff_bc)
                if key in last_seen:
                    ret = max(ret, i - last_seen[key])
                else:
                    last_seen[key] = i
            
            return ret
        
        r1 = case1()
        r2 = max(map(case2, "abc"))
        r3 = case3()
        return max(r1, r2, r3)

