'''
2023/01/27 daily challenge

dynamic programming approach

learnt from official solution 1
'''

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        ans = []

        for w in words:
            wlen = len(w)
            dp = [False] * (wlen+1)  # dp[i] indicates whether w[:i] is in words or can be concatenated from words.
            dp[0] = True  # an empty string can always be contatenated by nothing.
            # iterate from the first character
            for i in range(1, wlen+1):
                # check if the substring of w[:i] can be concatenated
                '''
                do not iterate j from 0 if we are verifying the full w word
                because w[0:wlen] == w is always in wordSet
                which is not sufficient unless there are multiple substrings in the dictionary.
                '''
                j = 1 if i==wlen else 0
                '''
                if dp[i] (w[:i], as a prefix of w) was verified a dictonary word
                or able to be concatenated in the previous for-loop,
                then no need to check the substrings of w[:i] again.
                '''
                while(not(dp[i]) and j < i):
                    '''
                    if both dp[j] (the status of the prefix w[:j]) and w[j:i] (the suffix)
                    are verified a dictonary word or able to be concatenated,
                    we say the substring w[:i] is a dictionary word or a concatenated word.
                    '''
                    dp[i] = dp[j] and w[j:i] in wordSet
                    j += 1
            if dp[wlen]:
                '''
                if the dp status of the full word w was verified as a concatenated word,
                it's a valid word of answer.
                '''
                ans.append(w)

        return ans

