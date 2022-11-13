'''
2022/11/13 daily challenge

pythonic oneliner
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        # the inline loop is to kill leading, trailing, and duplicate spaces.
        return ' '.join(sub for sub in reversed(s.split(' ')) if sub)

