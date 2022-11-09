'''
2022/11/09 daily challenge

stack approach, learnt from official solution

the instance-level stack keeps all prices greater or equal to the price from last next() call,
and the next() pops only smaller or equal prices & accumulate all popped span days
because popped span days is always a part of current price's span days.

e.g.
input: price=85

stack:
price=75, span=4 popped
price=80, span=1 popped

so the span of price=85 is
1 (itseif) + 4 (price=75) + 1 (price=80) = 6 days

note the definition of the span days is starting from **today** and going backward.
'''


class StockSpanner:
    def __init__(self):
        self.stack = []  # element=(price, span days)

    def next(self, price: int) -> int:
        span = 1  # today is also part of span.
        
        while self.stack and self.stack[-1][0] <= price:
            # accumulate popped span days
            span += self.stack.pop()[1]
        
        # push current price to the stack for further bigger price's reference.
        self.stack.append((price, span))
        return span

