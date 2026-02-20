'''
2026/02/20 daily challenge

divide and conquer approach

rearrange every valid prefix recursively,
make every substring in "1...0" form,
and sort substrings in lexicographically descending order.
'''


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        subs = []
        balance_count = 0
        si = 0

        for i, c in enumerate(s):
            if c == '1':
                balance_count += 1
            else:
                balance_count -= 1

            if balance_count == 0:
                inner = self.makeLargestSpecial(s[si+1:i])
                subs.append("1" + inner + "0")
                si = i + 1
        subs.sort(reverse=True)
        return ''.join(subs)

