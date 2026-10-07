'''
2026/10/07 daily challenge

brute force all bitmasks approach

Runtime=8448ms, Beats 5.03%
'''


class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        if s.count('(') == 0 or s.count(')') == 0:
            # hard-coded corner cases
            return [''.join([c for c in s if c.isalpha()])]

        def validate(slist):
            diff = 0
            for c in slist:
                if c == '(':
                    diff += 1
                elif c == ')':
                    diff -= 1
                    if diff < 0:
                        return False
            return diff == 0

        bracket_idxs = [i for i, c in enumerate(s) if not c.isalpha()]
        min_rm = bracket_counts = len(bracket_idxs)

        seen = set()
        for mask in range((1 << bracket_counts) -1, -1, -1):
            # removal set bit count
            rm_count = mask.bit_count()
            if rm_count > min_rm:
                continue

            slist = []
            j = 0
            for i, c in enumerate(s):
                if j < bracket_counts and bracket_idxs[j] == i:
                    jmask = 1 << j
                    j += 1
                    if mask & jmask:
                        # current bracket is marked removed
                        continue
                slist.append(c)
            if validate(slist):
                if rm_count < min_rm:
                    min_rm = rm_count
                    seen.clear()
                seen.add(''.join(slist))
        if not seen:
            return [""]
        return list(seen)

