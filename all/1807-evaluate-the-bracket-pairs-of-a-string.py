'''
2026/09/26 daily challenge

enumeration + hash dictionary approach
'''


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ans = []
        d = {k: v for k, v in knowledge}

        chunk_start = 0
        for i, c in enumerate(s):
            if c == '(':
                ans.append(s[chunk_start:i])
                chunk_start = i + 1
            elif c == ')':
                key = s[chunk_start:i]
                ans.append(d.get(key, '?'))
                chunk_start = i + 1

        if chunk_start != len(s):
            ans.append(s[chunk_start:])

        return ''.join(ans)


'''
pythonic built-in string formation approach
'''


import collections


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = collections.defaultdict(lambda: '?')
        for k, v in knowledge:
            d[k] = v

        s = s.replace('(', '{').replace(')', '}')

        return s.format_map(d)

