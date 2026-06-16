'''
2026/06/16 daily challenge

deque + flag approach
'''


import collections


class Solution:
    def processStr(self, s: str) -> str:
        q = collections.deque()
        rev_flag = 0

        for c in s:
            if c == '%':
                rev_flag ^= 1
            elif c == '#':
                if rev_flag:
                    q.extendleft(list(q)[::-1])
                else:
                    q.extend(list(q))
            elif c == '*':
                if not q:
                    continue
                if rev_flag:
                    q.popleft()
                else:
                    q.pop()
            else:
                if rev_flag:
                    q.appendleft(c)
                else:
                    q.append(c)
        return ''.join(list(q)[::-1] if rev_flag else list(q))


'''
simulation approach

trivial version runs faster.
'''


class Solution:
    def processStr(self, s: str) -> str:
        arr = []
        for c in s:
            if c == '%':
                arr.reverse()
            elif c == '#':
                arr = arr + arr
            elif c == '*':
                if arr:
                    arr.pop()
            else:
                arr.append(c)
        return ''.join(arr)

