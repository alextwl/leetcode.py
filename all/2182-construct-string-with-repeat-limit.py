'''
2024/12/17 daily challenge

counter + stack approach
'''


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        a = ord('a')
        # alphabet counter, also a stack in alphabetical order
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - a] += 1

        ans = []
        prev = -1
        repeat = 0
        while cnt:
            # remove exhausted alphabets
            while cnt and not cnt[-1]:
                cnt.pop()
            # select next char
            i = len(cnt) - 1
            while cnt and i >= 0:
                if cnt[i] and (i != prev or repeat < repeatLimit):
                    ans.append(chr(i + a))
                    cnt[i] -= 1
                    repeat = 1 if i != prev else repeat + 1
                    prev = i
                    break
                else:
                    i -= 1
            else:
                # all alphabets exhausted
                break
        return ''.join(ans)

