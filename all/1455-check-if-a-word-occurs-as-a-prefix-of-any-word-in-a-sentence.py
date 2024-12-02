'''
2024/12/02 daily challenge

finite-state machine approach
'''


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        flag = True  # a switch of word matching
        word_index = 1
        word_len = 0
        target_len = len(searchWord)
        for i, c in enumerate(sentence):
            if c == ' ':
                flag = True
                word_index += 1
                word_len = 0
            elif flag:
                if c == searchWord[word_len]:
                    word_len += 1
                    if word_len == target_len:
                        return word_index
                else:
                    flag = False
        return -1


'''
pythonic ver
'''


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        for i, w in enumerate(sentence.split(), start=1):
            if w[:n] == searchWord:
                return i
        return -1

