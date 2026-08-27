'''
2026/08/27 daily challenge

counter approach
'''


ASCII_A = ord('a')


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n, m = len(s), len(target)
        ctr = [0] * 26

        for asc in map(ord, s):
            ctr[asc - ASCII_A] += 1
        for asc in map(ord, target):
            ctr[asc - ASCII_A] -= 1

        for i in range(m - 1, -1, -1):
            curr = ord(target[i]) - ASCII_A
            ctr[curr] += 1

            # insufficient chars, cannot form target[:i]
            if any(v < 0 for v in ctr):
                continue

            # find next available char for next permutation
            j = -1
            for k in range(curr + 1, 26):
                if ctr[k]:
                    j = k
                    break
            else:
                continue

            ctr[j] -= 1

            prefix = target[:i]
            center = chr(j + ASCII_A)
            suffices = []
            for c, v in enumerate(ctr):
                if v:
                    suffices.append(chr(c + ASCII_A) * v)

            return prefix + center + ''.join(suffices)

        # no greater permutation available
        return ''

