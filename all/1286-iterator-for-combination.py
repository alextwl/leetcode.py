'''
simulation approach
'''


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.charset = characters
        self.max_digit = len(characters) - 1
        self.comb_len = combinationLength
        # use self.charset indices as enumeration of characters
        self.next_comb = list(range(combinationLength))
        self.avail_set = set(range(len(characters))) - set(self.next_comb)
        self.exhausted = False

    def next(self) -> str:
        s = ''.join(self.charset[d] for d in self.next_comb)

        while self.next_comb:
            digit = self.next_comb.pop()
            self.avail_set.add(digit)
            if digit >= self.max_digit:
                continue
            # each character in the suffix of the next combination
            # should be lexicographically greater than current (popped) char.
            # if not, pop one more char in the next iteration.
            candidates = sorted(d for d in self.avail_set if d > digit)
            diff_len = self.comb_len - len(self.next_comb)
            if len(candidates) >= diff_len:
                for d in candidates[:diff_len]:
                    self.next_comb.append(d)
                    self.avail_set.remove(d)
                break
        else:
            self.exhausted = True

        return s

    def hasNext(self) -> bool:
        return not self.exhausted

