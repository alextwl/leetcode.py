'''
intuitive approach.

official hint 2 helps: wrote helper1000() for converting num grouped by 3 digits to English words.
'''

class Solution:
    def numberToWords(self, num: int) -> str:
        words = {'1': "One", '2': "Two", '3': "Three",
                 '4': "Four", '5': "Five", '6': "Six",
                 '7': "Seven", '8': "Eight", '9': "Nine",
                 '10': "Ten", '11': "Eleven", '12': "Twelve",
                 '13': "Thirteen", '14': "Fourteen", '15': "Fifteen",
                 '16': "Sixteen", '17': "Seventeen", '18': "Eighteen",
                 '19': "Nineteen", '20': "Twenty", '30': "Thirty",
                 '40': "Forty", '50': "Fifty", '60': "Sixty",
                 '70': "Seventy", '80': "Eighty", '90': "Ninety"}
        
        thousand_words = {1: "Thousand", 2: "Million", 3: "Billion"}
        
        def helper1000(s: str) -> str:
            '''
            Convert a string of up to 3 digit (reversed) to English words.
            '''
            slen = len(s)
            
            if slen == 1:
                return words[s]
            ret = []
            if slen == 3 and s[2] != '0':
                ret.extend([words[s[2]], "Hundred"])
            if s[1::-1] in words:
                ret.append(words[s[1::-1]])
            elif s[1] != '0':
                ret.extend([words[s[1] + '0'], words[s[0]]])
            elif s[0] != '0':
                ret.append(words[s[0]])
                
            return ' '.join(ret)
        
        if num == 0:
            # special case 0.
            return "Zero"
        
        ans = []
        
        # group every 3 digits reversely.
        str_num_rev = str(num)[::-1]
        groups = [str_num_rev[i:i+3] for i in range(0, len(str_num_rev), 3)]
        
        for grp_idx, grp_str in enumerate(groups):
            # convert every 3 digits to English words in batch.
            group_words = helper1000(grp_str)
            if group_words:
                if grp_idx > 0:
                    ans.append(thousand_words[grp_idx])
                ans.append(group_words)
        
        return ' '.join(reversed(ans))
