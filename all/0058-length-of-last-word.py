'''
2024/04/01 daily challenge
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        space_occured = False

        for c in s:
            if c == ' ':
                space_occured = True
            else:
                # if c.isalpha():
                if space_occured:
                    # reset the length of last word
                    ans = 0
                    space_occured = False
                ans += 1

        return ans


'''
pythonic oneliner ver
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # str.split() without delimiter specified splits
        # string by whitespace delimiter and
        # discards empty substrings automatically.
        return len(s.split()[-1])

