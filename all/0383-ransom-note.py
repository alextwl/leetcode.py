class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charcount = dict()
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for s in alphabets:
            charcount[s] = 1  # start from 1 not 0 for the convenience of later if condition.
        for s in magazine:
            charcount[s] += 1
        for s in ransomNote:
            charcount[s] -= 1
            if not charcount[s]:
                return False
        return True
