class Solution:
    def maximumTime(self, time: str) -> str:
        hh, h, _, mm, m = time
        
        # tens digit of hour
        if hh == '?':
            if h == '?':
                hh = '2'
            elif h > '3':
                hh = '1'
            else:
                hh = '2'

        # units digit of hour
        if h == '?':
            if hh == '2':
                h = '3'
            else:
                h = '9'

        # tens digit of minute
        if mm == '?':
            mm = '5'

        # units digit of minute
        if m == '?':
            m = '9'

        return "%s%s:%s%s" % (hh, h, mm, m)

