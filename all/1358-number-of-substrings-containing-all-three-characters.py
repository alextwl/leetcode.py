'''
2025/03/11 daily challenge

sliding window approach
'''


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = {c: 0 for c in "abc"}

        ans = 0
        i = 0
        for j, c in enumerate(s):
            cnt[c] += 1
            while i < j and all(cnt.values()):
                ans += n - j
                cnt[s[i]] -= 1
                i += 1        
        return ans


'''
track last position of each alphabet approach

when we have min(last positions),
we can form at least one valid substring
and more longer substrings by extending to the left.
'''


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = [-1] * 3  # the last positions of abc (0-indexed)
        ans = 0
        a = ord('a')
        for i, c in enumerate(s):
            cnt[ord(c) - a] = i
            # the last position is 0-indexed, convert to 1-indexed by plus 1.
            ans += min(cnt) + 1
        return ans

