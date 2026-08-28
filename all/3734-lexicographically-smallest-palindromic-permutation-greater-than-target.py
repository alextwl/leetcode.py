'''
2026/08/28 daily challenge

counter + greedy method approach
'''


ASCII_A = ord('a')


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        if n == 1:
            return s if s > target else ""

        ctr = [0] * 26
        for asc in map(ord, s):
            ctr[asc - ASCII_A] += 1

        center = ""  # determine the center char which freq is odd
        for i in range(26):
            if ctr[i] & 1:
                # odd
                if center:
                    # cannot form a palindrome because more than one odd found
                    return ""
                center = chr(i + ASCII_A)
            # half the amount for further palindrome construction
            ctr[i] >>= 1

        # stack for half palindrome to be constructed
        prefix = []

        def is_larger(next_char):
            half = prefix + [next_char]
            # fill remaining unused chars reversely
            for i in range(25, -1, -1):
                half.append(chr(i + ASCII_A) * ctr[i])

            t = half + [center] + half[::-1]

            return ''.join(t) > target

        # try to construct prefix prior to center char
        for i in range(n // 2):
            # fill chars in lexicographical order
            for j in range(26):
                if not ctr[j]:
                    continue
                ctr[j] -= 1
                curr_char = chr(j + ASCII_A)
                if is_larger(curr_char):
                    prefix.append(curr_char)
                    break
                else:
                    # cannot use curr_char
                    ctr[j] += 1
            else:
                # a valid palindrome lexicographically larger than target not found.
                return ""

            if prefix[i] > target[i]:
                # prefix is already larger than target, no need to search further.
                half = prefix.copy()
                # fill remaining unused chars in lexicographical order
                for j in range(26):
                    half.append(chr(j + ASCII_A) * ctr[j])
                t = half + [center] + half[::-1]
                return "".join(t)

        t = prefix + [center] + prefix[::-1]
        return "".join(t)

