'''
2023/04/12 daily challenge

stack approach
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for subpath in path.split('/'):
            if subpath == '.' or subpath == '':
                # stripped, does nothing
                pass
            elif subpath == '..':
                # up a level when the working directory is not a root level.
                # if stack is empty (== we are now at root level),
                # going one level up from the root is not allowed.
                if stack:
                    stack.pop()
            else:
                stack.append(subpath)

        return '/' + '/'.join(stack)

