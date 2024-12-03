'''
2024/12/03 daily challenge

string manipulation approach
'''


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ls = []
        prev = 0
        for i in spaces:
            ls.append(s[prev:i])
            prev = i
        ls.append(s[prev:])
        return ' '.join(ls)

