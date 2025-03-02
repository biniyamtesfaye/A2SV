# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url: str) -> None:
        # When visiting a new url, remove all forward history
        self.history = self.history[:self.current_index + 1]
        self.history.append(url)
        self.current_index += 1
        #Code by Binyam
    def back(self, steps: int) -> str:
        # Move back in history, ensuring we don't go past the first page
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        # Move forward in history, ensuring we don't go past the most recent page
        self.current_index = min(len(self.history) - 1, self.current_index + steps)
        return self.history[self.current_index]