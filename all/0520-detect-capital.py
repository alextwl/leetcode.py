'''
2023/01/02 daily challenge
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            # a word of length 1 is always valid.
            return True

        # declare an iterator.
        # we will not backtrace letters we've read.
        iter_word = iter(word)

        # determine the form rule of the input word
        if (0b100000 & ord(next(iter_word))):
            '''
            first letter is not a capital.
            all remaining letters should be lower-case.
            '''
            find_capitals = False
        else:
            if (0b100000 & ord(next(iter_word))):
                '''
                first letter is a capital, following a lower-case letter.
                all remaining letters should be lower-case.
                '''
                find_capitals = False
            else:
                # all letters should be upper-case.
                find_capitals = True

        # check word from the 2nd or 3rd letter.
        for c in iter_word:
            is_capital = not(0b100000 & ord(c))
            if find_capitals ^ is_capital:
                return False

        return True

