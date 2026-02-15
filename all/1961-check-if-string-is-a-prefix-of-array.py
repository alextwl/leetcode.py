class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        n = len(s)
        i = 0
        for w in words:
            j = i + len(w)
            if j > n or s[i:j] != w:
                return False
            i = j
            if i == n:
                break

        return i == n

