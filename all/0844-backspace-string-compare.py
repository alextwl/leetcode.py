'''
leetcode 75 lv1 day 14

reversed string approach

using reversed inputs is more convenient to match two texts at the same position
because we cannot predict current character may be backspaced later or not in the non-reversed input.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # declare reversed iterators first.
        sr, tr = reversed(s), reversed(t)
        sc = tc = ''

        while(sc is not None and tc is not None):
            '''
            fast-forward when we've read '#'.
            (equal to backspacing in non-reversed inputs.)
            '''
            backspace = 0
            for c in sr:
                if c == '#':
                    backspace += 1
                elif backspace > 0:
                    backspace -= 1
                else:
                    # non-backspaced sc is read.
                    sc = c
                    break
            else:
                sc = None

            backspace = 0
            for c in tr:
                if c == '#':
                    backspace += 1
                elif backspace > 0:
                    backspace -= 1
                else:
                    # non-backspaced tc is read.
                    tc = c
                    break
            else:
                tc = None

            # time to match.
            if sc != tc:
                # text mismatch found
                return False

        return True


'''
stack approach

follow the official hint
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def rebuild(text):
            '''
            strip backspace from the text.
            '''
            stack = []
            for c in text:
                if c == '#':
                    if stack:
                        # pop char only when stack is not empty.
                        # a backspace with no chars does nothing.
                        stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)

        # compare backspace-stripped strings of two inputs.
        return rebuild(s) == rebuild(t)


'''
2023/10/19 daily challenge

space=O(1) ver

actually it's space=O(n) because we cannot assign characters
to a string so we always convert string to a list of characters.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)

        i = 0
        for k in range(len(s)):
            if s[k] == '#':
                if i:
                    i -= 1
            else:
                s[i] = s[k]
                i += 1

        j = 0
        for k in range(len(t)):
            if t[k] == '#':
                if j:
                    j -= 1
            else:
                t[j] = t[k]
                j += 1

        return ''.join(s[:i]) == ''.join(t[:j])

