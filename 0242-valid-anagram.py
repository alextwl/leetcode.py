class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        
        # count occurances
        for c in s:
            sdict[c] = sdict.get(c, 0) + 1
        for c in t:
            tdict[c] = tdict.get(c, 0) + 1
        
        if set(sdict) != set(tdict):
            return False
        
        for key in sdict.keys():
            if sdict[key] != tdict.get(key, 0):
                return False
        
        return True

        # pythonic oneliner
        import collections
        return collections.Counter(s) == collections.Counter(t)
