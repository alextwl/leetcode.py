'''
2024/11/04 daily challenge
'''


class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        cnt = 0
        prev = word[0]
        for c in word:
            if prev != c or cnt == 9:
                comp.append(str(cnt))
                comp.append(prev)
                cnt = 1
                prev = c
            else:
                cnt += 1

        # append the last serial char and finalize it.
        comp.append(str(cnt))
        comp.append(prev)

        return ''.join(comp)

