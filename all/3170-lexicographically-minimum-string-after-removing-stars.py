'''
2025/06/07 daily challenge

stack + greedy method approach
'''


import collections


alphabets = [chr(ord('a') + i) for i in range(26)]


class Solution:
    def clearStars(self, s: str) -> str:
        indices = {c: list() for c in alphabets}
        arr = []

        for i, c in enumerate(s):
            if c == '*':
                # delete the smallest char which is also the nearest to the asterisk.
                for t in alphabets:
                    if indices[t]:
                        arr[indices[t].pop()] = ''
                        break
                arr.append('')
            else:
                indices[c].append(i)
                arr.append(c)
        return ''.join(arr)

