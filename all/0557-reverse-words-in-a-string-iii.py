'''
2022/09/22 daily challenge
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        # pythonic oneloner!
        return ' '.join([w[::-1] for w in s.split(' ')])

'''
intuitive way to swap chars manually
it's not efficient when doing on Python because
we cannot directly modify a single char in a string.
extra space for a list converted from input str is used.

time=O(2n), space=O(2n)
'''

class Solution2:
    def reverseWords(self, s: str) -> str: 
        last_space = -1
        slen = len(s)
        l = list(s)  # a char in a str cannot be assigned, so convert it to list first.
        
        for pos in range(0, slen+1):
            # find space or end of str
            if pos == slen or l[pos] == ' ':
                left = last_space + 1
                right = pos - 1
                while (left < right):
                    l[left], l[right] = l[right], l[left]
                    left += 1
                    right -= 1
                last_space = pos
        
        return ''.join(l)
