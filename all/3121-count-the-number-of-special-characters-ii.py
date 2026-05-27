'''
2026/05/27 daily challenge

hash set approach
'''


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        up_seen = set()
        low_seen = set()
        blacklist = set()

        for c in word:
            if c < 'a':
                # uppercase
                up_seen.add(c.lower())
            else:
                # lowercase
                if c in up_seen:
                    blacklist.add(c)
                else:
                    low_seen.add(c)

        valids = up_seen & low_seen - blacklist
        return len(valids)

