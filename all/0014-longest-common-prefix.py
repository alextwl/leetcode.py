class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        for idx in range(0,200):
            try:
                c = strs[0][idx]
            except:
                return prefix
            for txt in strs:
                try:
                    if txt[idx] != c:
                        return prefix
                except:
                    return prefix
            prefix += c

        return prefix
