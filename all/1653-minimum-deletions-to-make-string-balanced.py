'''
2024/07/20 daily challenge
2026/02/07 daily challenge

count b & a in different directions and minimize the sum of deletions. (3-pass ver)
'''


class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        
        # count a from right and b from left
        # the value is the number of chars to be deleted
        suffix_a = [0] * n
        prefix_b = [0] * n
        
        b_cnt = 0
        for i, c in enumerate(s):
            prefix_b[i] = b_cnt
            if c == 'b': b_cnt += 1
        
        a_cnt = 0
        for i, c in enumerate(reversed(s)):
            suffix_a[i] = a_cnt
            if c == 'a': a_cnt += 1
        suffix_a.reverse()
        
        min_ans = n
        for a, b in zip(suffix_a, prefix_b):
            min_ans = min(min_ans, a + b)
        
        return min_ans


'''
stack approach
'''


class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        ans = 0
        for c in s:
            if stack and stack[-1] == 'b' and c == 'a':
                # remove pairs of a previous 'b' and an incoming 'a'
                # which are out of groups of suffix-b & prefix-a substrings.
                stack.pop()
                ans += 1
            else:
                stack.append(c)
        return ans


'''
dynamic programming approach
'''


class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = [0] * (len(s) + 1)  # dp[i] = min deletions of s[:i]

        b_cnt = 0
        for i, c in enumerate(s):
            if c == 'b':
                dp[i+1] = dp[i]
                b_cnt += 1
            else:
                dp[i+1] = min(dp[i] + 1, b_cnt)  # min(remove a, keep a)

        return dp[-1]


'''
two prefix sums approach
'''


class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt_a = cnt_b = 0
        psum_a = [0]
        psum_b = [0]

        for c in s:
            if c == 'a':
                cnt_a += 1
            else:
                cnt_b += 1
            psum_a.append(cnt_a)
            psum_b.append(cnt_b)

        total_a = psum_a[-1]
        ans = len(s)
        for a, b in zip(psum_a, psum_b):
            ans = min(ans, b + (total_a - a))
        return ans

