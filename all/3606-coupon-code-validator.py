'''
2025/12/13 daily challenge

sorting with normalized list approach
'''


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # convert businessLine categories to number in the order which question asked
        bl2id = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        # verify isActive flag, code chars in [a-zA-Z0-9_], and category
        active_codes = [(bl, coupon) for coupon, bl, flag in zip(code, businessLine, isActive)
                        if flag and coupon.replace('_', 'A').isalnum() and bl in bl2id]
        active_codes.sort()
        return [coupon for _, coupon in active_codes]

