'''
2023/03/18 daily challenge
'''

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0
        self.terminal = 0

    def visit(self, url: str) -> None:
        next_pos = self.current + 1
        if next_pos >= len(self.history):
            self.history.append(url)
        else:
            self.history[next_pos] = url
        self.current = self.terminal = next_pos

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(self.terminal, self.current + steps)
        return self.history[self.current]

