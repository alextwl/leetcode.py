'''
2026/08/13 daily challenge

segment tree approach

learnt from official editorial 1:
https://leetcode.com/problems/longest-substring-of-one-repeating-character/editorial/#approach-1-segment-tree
'''


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree_size = n * 4
        prefix = [0] * tree_size
        suffix = [0] * tree_size
        maxlen = [0] * tree_size
        leftchr = [''] * tree_size
        rightchr = [''] * tree_size

        def build(u, l, r):
            if l == r:
                prefix[u], suffix[u], maxlen[u] = 1, 1, 1
                leftchr[u], rightchr[u] = s[l], s[l]
            else:
                mid = (l + r) >> 1
                build(u << 1, l, mid)
                build(u << 1 | 1, mid + 1, r)
                pushup(u, l, r)

        def pushup(u, l, r):
            mid = (l + r) >> 1
            left_len = mid - l + 1
            right_len = r - mid

            left, right = u << 1, u << 1 | 1
            leftchr[u] = leftchr[left]
            rightchr[u] = rightchr[right]

            prefix[u] = prefix[left]
            if prefix[left] == left_len and rightchr[left] == leftchr[right]:
                prefix[u] = prefix[left] + prefix[right]

            suffix[u] = suffix[right]
            if suffix[right] == right_len and rightchr[left] == leftchr[right]:
                suffix[u] = suffix[right] + suffix[left]

            maxlen[u] = max(maxlen[left], maxlen[right])
            if rightchr[left] == leftchr[right]:
                maxlen[u] = max(maxlen[u], suffix[left] + prefix[right])
        
        def update(u, l, r, pos, c):
            if l == r:
                leftchr[u], rightchr[u] = c, c
            else:
                mid = (l + r) >> 1
                if pos <= mid:
                    update(u << 1, l, mid, pos, c)
                else:
                    update(u << 1 | 1, mid + 1, r, pos, c)
                pushup(u, l, r)
        
        build(1, 0, n - 1)

        ans = []
        for i in range(len(queryIndices)):
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i])
            ans.append(maxlen[1])  # root value of segment tree == length of longest substring
        return ans

