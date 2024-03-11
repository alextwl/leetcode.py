'''
2024/03/11 daily challenger

counter approach

place all ordered chars in the beginning or the end of string,
and leave all chars not in order untouched.
'''


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_count = {c: 0 for c in order}
        other_chars = []

        # separate ordered chars & other chars
        for c in s:
            if c in order_count:
                order_count[c] += 1
            else:
                other_chars.append(c)

        permuted = ""
        for c in order:
            permuted += c * order_count[c]

        return permuted + ''.join(other_chars)

