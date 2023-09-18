class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.enc = encoding
        self.idx = 0  # the even index
        self.last_idx = len(encoding) - 2
        self.pos = 0  # the exhausted count of self.enc[self.idx+1]

    def next(self, n: int) -> int:
        while(self.idx <= self.last_idx):
            n -= self.enc[self.idx] - self.pos
            if n <= 0:
                self.pos = self.enc[self.idx] + n
                return self.enc[self.idx+1]
            
            # we need next repeated integer
            self.idx += 2
            self.pos = 0
        
        return -1

