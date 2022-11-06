'''
2022/08/16 daily challenge
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        scount = dict()
        firstseen = dict()
        
        for idx, char in enumerate(s):
            if char in scount:
                scount[char] += 1
            else:
                scount[char] = 1
                firstseen[char] = idx
        
        uniques = [firstseen[char] for char, count in scount.items() if count == 1]
        
        if not uniques:
            return -1
        return min(uniques)
