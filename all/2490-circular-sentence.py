'''
2024/11/02 daily challenge
'''


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        words.append(words[0])
        return all(words[i][-1] == words[j][0] for i, j in zip(range(len(words)-1), range(1,len(words))))

