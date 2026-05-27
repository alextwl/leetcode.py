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


'''
built-in search approach
'''


# generate all upper and lower alphabets
UPPERS = [chr(ord('A') + i) for i in range(26)]
LOWERS = [chr(ord('a') + i) for i in range(26)]


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        for up, low in zip(UPPERS, LOWERS):
            # find the first position of uppercase and last position of lowercase
            if up in word and low in word and word.find(up) > word.rfind(low):
                ans += 1
        return ans

