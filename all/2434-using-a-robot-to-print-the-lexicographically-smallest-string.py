'''
2025/06/06 daily challenge

stack + suffix smallest character (similar to prefix sum) approach

to make the string on paper lexicographically smallest,
queue each char of s in t and print top of t
if there's no further smaller character in s.
'''


class Solution:
    def robotWithString(self, s: str) -> str:
        # build a suffix smallest alphabet list for s.
        smallest = []
        suffix_smallest = s[-1]
        for curr in reversed(s):
            if curr < suffix_smallest:
                suffix_smallest = curr
            smallest.append(suffix_smallest)

        t = []
        p = []

        for curr, suffix_smallest in zip(s, reversed(smallest)):
            # suffix_smallest = smallest_alphabet(s[i:])
            while t and t[-1] <= suffix_smallest:
                # no more further alphabets smaller than top of t,
                # feel free to print it on paper.
                p.append(t.pop())
            if curr <= suffix_smallest:
                # current alphabet is the smallest,
                # output to t and print on paper immediately.
                p.append(curr)
            else:
                # we always output every char to t.
                t.append(curr)
        while t:
            p.append(t.pop())
        return ''.join(p)

