'''
brute-force set matching with sorted string

note there's constraint that no letters occurs more than once in any string,
so the sorting and string concatenation just work.
'''


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        ans = 0
        src_set = set()
        for src in startWords:
            src_set.add(''.join(sorted(src)))

        for dst in targetWords:
            w = ''.join(sorted(dst))
            for i in range(len(w)):
                if w[:i] + w[i+1:] in src_set:
                    # try to strip each char respectively to find if a start word exists.
                    ans += 1
                    break

        return ans

