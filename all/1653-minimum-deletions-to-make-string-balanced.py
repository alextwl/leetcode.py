'''
2024/07/20 daily challenge

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

