'''
2024/10/06 daily challenge

queue approach

note the question asks for inserting **AN** arbitrary sentence,
**NOT** two or more sentences, that means one prefix & suffix must
match the another one's, otherwise it's invalid.
'''


import collections


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        q1 = collections.deque(sentence1.split(' '))
        q2 = collections.deque(sentence2.split(' '))

        # match prefix words
        while q1 and q2 and q1[0] == q2[0]:
            q1.popleft()
            q2.popleft()

        # match suffix words
        while q1 and q2 and q1[-1] == q2[-1]:
            q1.pop()
            q2.pop()

        return not(q1) or not(q2)

