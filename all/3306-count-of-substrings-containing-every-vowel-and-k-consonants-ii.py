'''
2025/03/10 daily challenge

sliding window approach

convert the problem "exactly k consonants" into "at least k consonants" by
Exactly(k) = AtLeast(k) - AtLeast(k+1).
'''


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._count_at_least_k(word, k) - self._count_at_least_k(word, k + 1)
    
    def _count_at_least_k(self, word, k):
        n = len(word)
        vowel = {c: 0 for c in "aeiou"}
        vowel_cnt = 0
        consonant_cnt = 0
        ans = 0

        i = 0
        for j, c in enumerate(word):
            if c in vowel:
                vowel[c] += 1
                vowel_cnt += 1
            else:
                consonant_cnt += 1

            # shrink the window
            while consonant_cnt >= k and vowel_cnt >= 5 and all(vowel.values()):
                ans += n - j
                prev = word[i]
                if prev in vowel:
                    vowel[prev] -= 1
                    vowel_cnt -= 1
                else:
                    consonant_cnt -= 1
                i += 1

        return ans

