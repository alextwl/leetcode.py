'''
2023/09/26 daily challenge

two-pass + stack approach

similar to problem 1081.
'''


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        the position of each alphabet's last occurance in s.
        '''
        last_pos = {}
        for i, c in enumerate(s):
            last_pos[c] = i

        seen = set()
        stack = []
        
        for i, c in enumerate(s):
            if c not in seen:
                '''
                if c was not yet visited, before adding it to the stack,
                we need to pop all lexicographical larger characters from the stack
                (unless they have no more duplicates after i),
                so that we can make the stack the smallest in lexicographical order.
                '''
                while(stack and \
                      stack[-1] > s[i] and \
                      last_pos[stack[-1]] > i):
                    '''
                    there are remaining duplicates of
                    the last element in stack after s[i],
                    we also need to remove it from the seen set
                    so that the latter occurance of the char has chance to push back to the stack.
                    
                    '''
                    seen.remove(stack.pop())
                
                stack.append(c)
                seen.add(c)
        '''
        the final sequence of the stack is the smallest
        in lexicographical order.
        '''
        return ''.join(stack)

