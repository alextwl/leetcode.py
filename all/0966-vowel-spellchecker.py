'''
2025/09/14 daily challenge

hashset approach
'''


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def get_vowel_wildcards(s):
            arr = []
            for c in s:
                if c in 'aeiou':
                    arr.append('*')
                else:
                    arr.append(c)
            return ''.join(arr)

        exact_set = set(wordlist)
        cat1 = dict()  # category 1: capitalization dict  (lowercase: original word)
        cat2 = dict()  # category 2: vowel wildcard dict  (wildcard key: original word)
        for s in wordlist:
            lower = s.lower()
            if lower not in cat1:
                cat1[lower] = s

            key = get_vowel_wildcards(lower)
            if key not in cat2:
                cat2[key] = s

        ans = []
        for s in queries:
            if s in exact_set:
                ans.append(s)
                continue

            lower = s.lower()
            if lower in cat1:
                ans.append(cat1[lower])
                continue

            key = get_vowel_wildcards(lower)
            if key in cat2:
                ans.append(cat2[key])
            else:
                ans.append('')

        return ans

