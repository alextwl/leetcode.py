'''
stack approach

pop each char from leftmost and compare it with the last char of stack.
'''

import collections


class Solution:
    def removeDuplicates(self, s: str) -> str:
        orig = collections.deque(s)
        ans = []
        
        # initialize stack with first char.
        ans.append(orig.popleft())
        
        while(orig):
            c = orig.popleft()
            if ans and c == ans[-1]:
                '''
                if current char was equal to last char of stack,
                pop stack.
                '''
                ans.pop()
            else:
                # non-duplicate char, push to stack
                ans.append(c)
        
        return ''.join(ans)

